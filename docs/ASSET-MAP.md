# Unity 2019.4.29f1 asset map

Source: original user-supplied RollingSkyRemake-1.3.0r-Windows.zip, inspected without modifying it.

| Original path | Verified role | Next investigation |
| --- | --- | --- |
| `Rolling Sky Remake.exe` | Windows launcher | Preserve alongside its matching Data folder |
| `GameAssembly.dll` | IL2CPP compiled code | Inspect compatibility, do not replace blindly |
| `UnityPlayer.dll` | Unity runtime | Preserve |
| `Rolling Sky Remake_Data/globalgamemanagers` | Unity global configuration; contains version `2019.4.29f1` | Read serialized settings |
| `Rolling Sky Remake_Data/level0` through `level2` | Three Unity scene files | Identify menu/gameplay scenes |
| `Rolling Sky Remake_Data/sharedassets0.assets` through `sharedassets2.assets` | Scene-referenced serialized assets | Index sprites, textures, meshes, materials |
| `Rolling Sky Remake_Data/resources.assets` | Resources folder serialized assets | Search UI branding |
| `Rolling Sky Remake_Data/*.resS` | Streamed binary resource data | Keep paired with associated asset files |
| `Rolling Sky Remake_Data/il2cpp_data/Metadata/global-metadata.dat` | IL2CPP metadata | Identify menu classes |
| `Rolling Sky Remake_Data/StreamingAssets/level.rsr` | RSR file, 694 bytes | Determine custom format |
| `Rolling Sky Remake_Data/StreamingAssets/RunWay.rsr` | RSR file, 3,118,466 bytes | Determine custom format |

## Do not move the original runtime files

The paths above are the correct **runtime layout**, not editable Unity project folders. Unity expects these relationships to remain intact. Original game files should remain under `workspace/original-game/` (gitignored).

## Editable additions

- `branding/`: original logo and UI artwork
- `themes/`: original theme assets and manifests, once format is established
- `models/`: original meshes and textures
- `patches/`: reversible modification scripts and source, once tested
- `tools/`: extraction and analysis scripts

## Findings

- Unity engine: **2019.4.29f1**, read from `globalgamemanagers`.
- Scripting backend: **IL2CPP**, based on `GameAssembly.dll` and `il2cpp_data`.
- The ZIP contains three scene files and two `.rsr` files.
- `level.rsr` begins with a length-prefixed gzip segment; its full serialization format remains unknown.
- No UI replacement, game binary patch, or Windows gameplay test has yet been performed.

## Next work

Extract the original ZIP locally with `tools/extract_and_inventory.py`, index serialized Unity object types/names using a Unity 2019-compatible asset inspection library, locate the exact logo and menu resources, and create a reversible test patch.
