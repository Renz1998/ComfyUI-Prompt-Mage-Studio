# Your first Studio session

[← Back to Prompt Mage Studio](README.md)

1. Clone Studio into `ComfyUI/custom_nodes` using the command in the README.
2. Install its requirements with the Python that runs ComfyUI. For Windows portable, run this from the portable installation's root:

   ```powershell
   .\python_embeded\python.exe -m pip install -r .\ComfyUI\custom_nodes\ComfyUI-Prompt-Mage-Studio\requirements.txt
   ```

3. Restart ComfyUI when idle and refresh the browser. Add **Prompt Mage Studio · Grimoire**.
4. Choose your assistant in Settings. For Local Qwen, select a compatible installed model or connect a compatible CLIP loader. API providers need a key entered in the masked key panel.
5. Start a conversation. Try: “Help me plan three scenes of a traveling mage arriving at a lantern-lit inn. Keep the same green cloak and leather satchel.”
6. Refine the idea, choose a style, and add references. Sending chat does not start your image sampler.
7. Choose **Use this prompt** on a reply. Connect Spell Scroll to your image workflow to generate from the applied selection.

For an image series, open the [Grimoire → Foundry example](workflows/grimoire-to-foundry.json). Select installed model filenames, discuss the project, then explicitly send the brief to Foundry. Preview and approve its plan before starting production.

Models are not included. Local chat needs generation-capable weights; image inputs also need vision support. Production examples require MOSS models and additional sampling nodes. [Workflow guide →](workflows/README.md)

Existing Prompt Mage user? [Copy your data →](docs/MIGRATION.md)
