from test_regressions import plugin
import json
import os
import unittest
from urllib.error import HTTPError
from unittest.mock import MagicMock, patch
import torch
from dart_plugin.py.dart.venice_assistant import VeniceEncoder, MODELS, set_session_key, key_status, resolve_key
from dart_plugin.py.dart.openai_assistant import OpenAIRequestError, key_status as openai_status


class VeniceTests(unittest.TestCase):
    def tearDown(self):
        set_session_key('')

    def request(self, model=None, choice=None, error=None, **kwargs):
        opener = MagicMock()
        if error:
            opener.open.side_effect = error
        opener.open.return_value.__enter__.return_value.read.return_value = json.dumps({
            'choices': [choice or {'finish_reason':'stop','message':{'content':'A red mug.', 'reasoning_content':'PRIVATE'}}],
            'usage': {'prompt_tokens':10,'completion_tokens':20,'completion_tokens_details':{'reasoning_tokens':5}}
        }).encode()
        with patch.dict(os.environ, {'VENICE_API_KEY':'test-not-real'}), patch('dart_plugin.py.dart.venice_assistant.build_opener', return_value=opener):
            encoder = VeniceEncoder(model or next(iter(MODELS)))
            result = encoder.execute(prompt='Describe a mug', **kwargs)
        return encoder, result, opener

    def test_key_isolation_and_no_readback(self):
        before = openai_status()
        with patch.dict(os.environ, {}, clear=True):
            set_session_key('sk-test-not-a-real-venice-key')
            self.assertTrue(key_status()['configured'])
            self.assertNotIn('sk-test', str(key_status()))
            self.assertEqual(resolve_key('VENICE_API_KEY'), 'sk-test-not-a-real-venice-key')
            self.assertFalse(os.environ.get('VENICE_API_KEY'))
        self.assertEqual(openai_status(), before)

    def test_payload_thinking_usage_and_vision(self):
        encoder, result, opener = self.request(thinking=True, image=torch.zeros(1,16,16,3))
        request = opener.open.call_args.args[0]
        self.assertEqual(request.full_url, 'https://api.venice.ai/api/v1/chat/completions')
        payload = json.loads(request.data)
        self.assertEqual(payload['model'], 'deepseek-v4-1-flash-1017-uncensored')
        self.assertEqual(payload['venice_parameters']['disable_thinking'], False)
        self.assertEqual(payload['reasoning_effort'], 'high')
        self.assertTrue(payload['messages'][1]['content'][1]['image_url']['url'].startswith('data:image/png;base64,'))
        self.assertEqual(result.args, ['A red mug.'])
        self.assertEqual(encoder.calls[0]['reasoning_tokens'], 5)
        self.assertNotIn('PRIVATE', str(result))
        self.assertEqual(opener.open.call_count, 1)

    def test_truncated_refused_and_empty_responses_fail(self):
        for choice in [dict(finish_reason='length',message={'content':'partial'}),
                       dict(finish_reason='content_filter',message={'content':''}),
                       dict(finish_reason='stop',message={'content':'','reasoning_content':'private'})]:
            with self.assertRaises(OpenAIRequestError):self.request(choice=choice)

    def test_non_thinking_and_archmage_registration(self):
        _, _, opener = self.request(thinking=False)
        payload = json.loads(opener.open.call_args.args[0].data)
        self.assertEqual(payload['venice_parameters']['disable_thinking'], True)
        self.assertNotIn('reasoning_effort', payload)
        schema = plugin.NODE_CLASS_MAPPINGS['PromptMageStudioArchmageBeta'].INPUT_TYPES()
        self.assertIn('Venice API', schema['optional']['assistant_backend'][0])
        self.assertEqual(schema['optional']['venice_model'][0], list(MODELS))

    def test_billing_and_auth_errors_do_not_echo_provider_secrets(self):
        import io
        for code in (401, 402, 429):
            with self.assertRaises(OpenAIRequestError) as caught:
                self.request(error=HTTPError('https://api.venice.ai/api/v1/chat/completions', code,
                                            'secret-key-detail', {}, io.BytesIO(b'private provider body')))
            self.assertIn(str(code), str(caught.exception))
            self.assertNotIn('secret', str(caught.exception))
            self.assertNotIn('private', str(caught.exception))

    def test_multiple_reference_images_share_one_request(self):
        _,_,opener=self.request(image=[torch.zeros(1,16,16,3),torch.ones(1,16,16,3)])
        payload=json.loads(opener.open.call_args.args[0].data)
        self.assertEqual([part['type'] for part in payload['messages'][1]['content']],['text','image_url','image_url'])

    def test_foundry_profiles_and_brief_transport(self):
        from dart_plugin.py.dart import foundry, foundry_ai
        from dart_plugin.py.nodes.production_brief import PromptMageGrimoireBrief
        profile='Venice · '+next(iter(MODELS))
        self.assertIn(profile,foundry.ASSISTANTS)
        self.assertIn(profile,foundry.REVIEWERS)
        config=foundry.review_settings(profile,{'assistant_backend':'Local Qwen'})
        self.assertEqual(config['assistant_backend'],'Venice API')
        with patch.dict(os.environ,{'VENICE_API_KEY':'synthetic-only'}):
            self.assertIsInstance(foundry_ai.encoder_for(config),VeniceEncoder)
        self.assertIn('venice_model',PromptMageGrimoireBrief.INPUT_TYPES()['optional'])

    def test_persistent_key_replace_remove_isolation(self):
        import tempfile,sys
        from types import SimpleNamespace
        from dart_plugin.py.dart.venice_assistant import set_persistent_key
        from dart_plugin.py.dart.credentials import credential_path,store_key
        with tempfile.TemporaryDirectory() as d,patch.dict(sys.modules,{'folder_paths':SimpleNamespace(get_user_directory=lambda:d)}),patch.dict(os.environ,{},clear=True):
            store_key('deepseek','other-provider-test')
            set_persistent_key('VENICE_INFERENCE_KEY_synthetic-only')
            set_session_key('')
            self.assertTrue(key_status()['saved_configured'])
            set_persistent_key('VENICE_INFERENCE_KEY_replacement')
            self.assertNotIn('synthetic-only',credential_path('venice').read_text())
            set_persistent_key('')
            self.assertFalse(credential_path('venice').exists())
            self.assertTrue(credential_path('deepseek').exists())
