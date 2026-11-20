# Studio example workflows

[← Back to Prompt Mage Studio](../README.md)

Download a JSON file and drag it onto the ComfyUI canvas, or open it through the workflow menu.

| Workflow | Purpose |
| --- | --- |
| [Grimoire → Foundry](grimoire-to-foundry.json) | Main starting point: chat, transfer a brief, approve a plan and produce a series |
| [Single-frame Foundry](experimental/01-foundry-single-frame-moss.json) | Test composition, rendering and visual review before a larger run |
| [Experimental Grimoire → Foundry](experimental/02-grimoire-to-foundry-moss.json) | Separate MOSS production example for experimentation |

## Before running

- Install Studio and any missing custom nodes shown by ComfyUI. Keep original Prompt Mage if you add DART tools.
- Select your diffusion model, text encoder, VAE and accelerator LoRA filenames. The examples contain no character LoRA.
- These graphs target MOSS Image. See the [MOSS project](https://github.com/OpenMOSS/MOSS-Image) and [Qwen checkpoints](https://huggingface.co/Qwen) for model sources. Weights are not bundled.
- Local Qwen is the saved assistant default. Use a compatible generation-capable encoder with vision weights for references, or configure an API provider.
- Connect matching canvas width and height to the prompt and image-generation paths.

## A first production run

1. Discuss the project in Grimoire and settle the visual direction.
2. Choose **Send brief → Foundry** to transfer an explicit snapshot. Later chat does not change that snapshot.
3. Preview the plan and inspect frames, styles, checks and run limits.
4. Approve the plan. Automatic mode renders, reviews, retries as needed and advances on a pass. Manual controls let you inspect decisions yourself.
5. Inspect accepted images before publishing. Review scores are fallible; API use is billed by the provider.

Start with one frame and modest limits before producing a collection. [Validation and limits →](../TESTING.md)
