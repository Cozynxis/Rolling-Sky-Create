# Rolling Sky Create

A planned expansion of Rolling Sky Remake 1.3.0r, focused on custom branding, updated UI, level themes, models, and new features.

## Current status

**Research and project setup only.** No gameplay, menus, Unity assets, or executable have been modified yet.

The `main` branch currently contains six split 7z archive volumes of the original Windows game. These are **not** editable source code. Keep the original build intact and work on a separate copy.

## Roadmap

1. Identify the Unity version, menu scenes, textures, fonts, and asset bundles.
2. Test whether asset replacement can update the logo and menu graphics.
3. Evaluate a compatible IL2CPP runtime extension for interactive UI changes.
4. Add new theme and model assets through a validated loading pipeline.
5. Package an optional patch/installer and test it on Windows.

## Project layout

- `docs/` — reverse-engineering notes and test plan
- `branding/` — original Rolling Sky Create artwork
- `patches/` — future patch source and scripts (not yet implemented)
- `themes/` — future theme manifests and assets
- `models/` — future original model assets

## Important

The included archives contain a third-party game build. Before redistributing them publicly, confirm you have permission from the rights holder. Prefer publishing only original artwork, mod code and patch files that do not contain copyrighted game assets.
