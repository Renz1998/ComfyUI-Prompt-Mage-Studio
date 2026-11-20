# Credits and provenance

Prompt Mage Studio is maintained by [Renz1998](https://github.com/Renz1998). It is the separate Grimoire, Foundry and scene-assistance pack, split from Prompt Mage. **Studio does not include DART tag nodes or require DART models or the original pack for its own nodes.** DART tools remain available separately in [the original Prompt Mage pack](https://github.com/Renz1998/ComfyUI-Prompt-Mage).

Studio retains code derived from nkchocoai/ComfyUI-Dart through Prompt Mage. The attribution below records that source-code lineage; it does not describe bundled DART functionality. The Studio name does not imply authorship of the underlying models.

| Contribution | Creator / source |
| --- | --- |
| Upstream source-code foundation, via Prompt Mage | [nkchocoai and contributors](https://github.com/nkchocoai/ComfyUI-Dart) |
| Qwen language/vision models | [Qwen team](https://huggingface.co/Qwen), including [Qwen3-VL 4B Instruct](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct); checkpoint conversion authors retain their own credits |
| MOSS-Image model and native layout format | [OpenMOSS team](https://github.com/OpenMOSS/MOSS-Image), [layout guide](https://github.com/OpenMOSS/MOSS-Image/blob/main/USERGUIDE.md) |
| Native model loading, text generation, offloading and graph frontend | [ComfyUI contributors](https://github.com/Comfy-Org/ComfyUI) |
| Transformers model runtime | [Hugging Face and contributors](https://github.com/huggingface/transformers) |

## Source and models

The original [GPL-3.0 LICENSE](LICENSE) is retained unchanged for this derived node pack. Studio was published as a separate repository; the linked upstream repositories document its earlier source history. Model weights are not bundled; the software license does not replace each model's own license, access conditions or attribution. Refer to the specific model/checkpoint card before redistribution. MOSS-Image is a downstream target, not a model trained by this project.

MOSS output options are formatting choices, not endorsements or renamed model releases. Prompt Mage Studio is an independent community project.

## Separate DART project

The original Prompt Mage pack includes DART tools based on models by [p1atdev](https://huggingface.co/p1atdev). Those tools and models are outside Studio's node selection and installation requirements. Workflows that explicitly use DART nodes still need the original pack.
