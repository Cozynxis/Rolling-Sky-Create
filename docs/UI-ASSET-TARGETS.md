# UI asset targets from user-provided UnityPy scan

Generated from `unity-assets.json` and `ui-candidates.json`. These are **serialized object IDs**, not disk paths. They must be resolved inside the original Unity asset files.

## Main menu scene

| File | Object type | Path ID | Name |
|---|---|---:|---|
| `Rolling Sky Remake_Data/level0` | GameObject | 21 | MainMenu |
| `Rolling Sky Remake_Data/level0` | GameObject | 14 | Canvas |
| `Rolling Sky Remake_Data/level0` | GameObject | 227 | logo_scale_offset |
| `Rolling Sky Remake_Data/level0` | GameObject | 235 | logo_video |
| `Rolling Sky Remake_Data/level0` | GameObject | 266 | logo_anim |
| `Rolling Sky Remake_Data/level0` | GameObject | 405 | logo_buttons |
| `Rolling Sky Remake_Data/level0` | GameObject | 178 | Level Selector |
| `Rolling Sky Remake_Data/level0` | GameObject | 449 | LevelsFeatured |

## Candidate logo resources

| File | Object type | Path ID | Name |
|---|---|---:|---|
| `Rolling Sky Remake_Data/sharedassets0.assets` | Texture2D | 65 | logodefault |
| `Rolling Sky Remake_Data/sharedassets0.assets` | Material | 7 | logoBackground |
| `Rolling Sky Remake_Data/sharedassets0.assets` | Material | 8 | logoMaterial |
| `Rolling Sky Remake_Data/sharedassets0.assets` | Material | 9 | logoPlaceholderMaterial |

## Other UI resources

- `sharedassets0.assets` Texture2D 57: `play`
- `sharedassets0.assets` Texture2D 64: `options`
- `sharedassets0.assets` Texture2D 93: `ButtonBg`
- `sharedassets0.assets` Texture2D 71: `Menu-A`
- `sharedassets0.assets` Texture2D 72: `Menu-B`
- `sharedassets0.assets` Texture2D 39: `Menu-C`
- `sharedassets0.assets` Texture2D 62: `Menu-D`
- `sharedassets0.assets` Texture2D 47: `Menu-E`
- `sharedassets0.assets` Texture2D 25: `Menu-F`

## Caution

The scan contains names and object IDs but **does not establish which components reference which assets**, or whether a candidate texture is visible in the startup menu. Do not overwrite any serialized objects until their references and dimensions are verified. No patched executable has been built or tested.
