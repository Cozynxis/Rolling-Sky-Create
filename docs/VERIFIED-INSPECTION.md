# Verified inspection of the uploaded Windows build

Inspected the user-provided `RollingSkyRemake-1.3.0r-Windows.zip` directly.

- 65 ZIP entries (including directories)
- Unity runtime: `2019.4.29f1` (verified in `globalgamemanagers`)
- `globalgamemanagers`: 514,132 bytes
- `global-metadata.dat`: 5,701,524 bytes
- IL2CPP metadata contains these byte strings (not yet confirmed as scene instances):
  - `MainMenu` at byte offset 165,822
  - `Canvas` at byte offset 83,007
  - `LevelManager` at byte offset 928,600
  - `Rolling Sky` at byte offset 121,736
- Three Unity scene files: `level0`, `level1`, `level2`
- Two StreamingAssets files: `level.rsr`, `RunWay.rsr`

## Limitations

This environment could inspect the ZIP and metadata, but cannot currently install the UnityPy dependency required for serialized Unity object inspection. The object names and asset-to-scene mapping are therefore **not verified**. Do not assume a specific logo or menu object can be replaced yet.

The project is a compiled Unity IL2CPP Windows game, not a Unity source project. Changing visuals will require compatible serialized-asset replacement or a separately tested runtime mod. No such replacement has yet been proven safe or functional.

## Practical next step

On Windows, install Python and run:

```powershell
py -m pip install UnityPy
py tools/extract_and_inventory.py "C:\\path\\to\\RollingSkyRemake-1.3.0r-Windows.zip"
py tools/scan_unity_assets.py workspace/original-game
```

The scan writes `workspace/unity-assets.json` and `workspace/ui-candidates.json` without changing the original game. These reports can be used to identify exact logo and UI object IDs before any patch is applied.
