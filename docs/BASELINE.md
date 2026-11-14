# Baseline inspection — Rolling Sky Remake 1.3.0r

Source: user-provided `RollingSkyRemake-1.3.0r-Windows.zip`.

Confirmed top-level entries include:

- `Rolling Sky Remake.exe`
- `GameAssembly.dll`
- `Rolling Sky Remake_Data/`
- `Rolling Sky Remake_Data/globalgamemanagers`
- `Rolling Sky Remake_Data/globalgamemanagers.assets`
- `Rolling Sky Remake_Data/il2cpp_data/`

The presence of `GameAssembly.dll` and `il2cpp_data` indicates a Unity IL2CPP Windows build.

The existing EXE and `Rolling Sky Remake_Data` directory form a matched pair; do not rename the executable alone.

## Investigation still required

- Exact Unity editor/runtime version
- UI scene names, serialized Canvas objects, fonts and sprite assets
- Logo and splash screen asset locations
- Theme/model format and loading mechanism
- Compatibility of runtime mod loaders

No claim of working asset modification or runtime injection is made at this stage.
