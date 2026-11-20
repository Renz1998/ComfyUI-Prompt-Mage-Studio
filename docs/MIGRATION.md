# Move existing work to Studio

[← Back to Prompt Mage Studio](../README.md)

Studio uses separate node IDs and saves data under `prompt_mage_studio` in your ComfyUI user directory. Original data remains under `prompt_mage`. Keep the original pack for old workflows and DART nodes.

Back up your user directory and leave ComfyUI idle or closed while copying. Run these commands from Studio using your ComfyUI Python. Replace the example user-directory path with your real one.

**Preview first — no files are written:**

```sh
python tools/migrate.py --user-directory "D:/AI/User"
```

**Copy missing data and create Studio workflow copies:**

```sh
python tools/migrate.py --user-directory "D:/AI/User" --apply
```

**Optionally copy provider keys on this trusted machine:**

```sh
python tools/migrate.py --user-directory "D:/AI/User" --apply --include-keys
```

The tool preserves originals and skips existing destinations. It converts Studio-owned node types in top-level JSON workflows under `default/workflows`, writing separate ` - Studio.json` copies. Nested workflow folders are not scanned. DART nodes remain unchanged and require the original pack.

Inspect copies before running. Installed model names, local paths and custom nodes may need adjustment, especially on another server. Keep credentials out of shared ZIPs and Git repositories.
