# Local validation · 2026-11-18

- 81 Foundry regression tests and 30 Grimoire tests passed.
- Foundry UI and production-bridge frontend tests passed.
- Original and Studio packs coexist with 32 and 13 independent registrations; both route namespaces respond.
- Real browser inspection confirmed Grimoire chat, Foundry controls and the independent review-model selector render together. The isolated CPU test server lacked production model paths; its model-file warnings were expected.
- Installed Studio alongside the original pack in local ComfyUI. Migration copied missing user data, workflow copies and provider keys without changing originals.
- Native GPU Grimoire chat with Qwen3.5 9B W4A8 passed in 3.9 seconds, using local inference and Studio conversation storage.
- The updated ComfyUI environment passed pip dependency checks.
- Separate MiniMax H3 Image tests passed for 1 MP text generation, 4 MP text generation, single-reference editing, two-reference editing and local prompt expansion. No claim is made for RunPod or 16 MP GPU testing.

Registry publication remains pending. These results do not imply every optional API provider was retested or that all possible historical workflows migrate without manual model-path adjustment.

## Venice API · 2026-11-20

- Live model listing authenticated and confirmed vision, multiple-image and reasoning capabilities for `deepseek-v4-1-flash-1017-uncensored`.
- Live neutral chat returned the requested marker; image recognition correctly identified a red square; a thinking-enabled arithmetic request returned the correct answer. The last request did not report reasoning-token usage, so internal reasoning execution is not independently verified.
- Provider adapter, credential isolation/replacement/removal, model profiles and masked-key UI are covered by focused tests. No unrestricted-content behavior is claimed.
- Installed ComfyUI exposed Venice provider/model schemas and the saved-key status route. A live Grimoire turn produced validated MOSS JSON; a live Foundry request produced a one-frame plan with Venice selected for production and review. No diffusion-render sequence was run for this provider update.
- Regression checks passed: 81 Foundry tests, 30 Grimoire tests, 9 production-brief tests and 8 Venice tests; masked-key, Grimoire, Archmage, Foundry and production-bridge JavaScript checks passed.
