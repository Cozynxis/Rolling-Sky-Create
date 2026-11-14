#!/usr/bin/env python3
"""Read-only Unity asset inventory for a locally extracted Rolling Sky Remake build.

Requires: python -m pip install UnityPy
Run: python tools/scan_unity_assets.py workspace/original-game
Output: workspace/unity-assets.json and workspace/ui-candidates.json
"""
import argparse
import json
from collections import Counter
from pathlib import Path

SUFFIXES = (".assets",)
NAMES = ("globalgamemanagers", "level0", "level1", "level2")
KEYWORDS = ("menu", "logo", "title", "rolling", "sky", "button", "canvas",
            "level", "theme", "background", "music", "icon", "sprite", "font")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("game_dir", type=Path)
    args = parser.parse_args()
    try:
        import UnityPy
    except ImportError:
        raise SystemExit("Install UnityPy: python -m pip install UnityPy")
    game_dir = args.game_dir.resolve()
    if not game_dir.is_dir():
        raise SystemExit(f"Missing game directory: {game_dir}")
    results = []
    candidates = []
    for path in sorted(game_dir.rglob("*")):
        if not path.is_file() or not (path.name in NAMES or path.name.endswith(SUFFIXES)):
            continue
        relative = str(path.relative_to(game_dir))
        entry = {"file": relative, "size": path.stat().st_size, "types": {}, "objects": [], "error": None}
        try:
            env = UnityPy.load(str(path))
            types = Counter()
            for obj in env.objects:
                kind = obj.type.name
                types[kind] += 1
                record = {"path_id": str(obj.path_id), "type": kind}
                if kind in {"Texture2D", "Sprite", "GameObject", "Material",
                            "AudioClip", "TextAsset", "Mesh", "Font", "AssetBundle"}:
                    try:
                        data = obj.read()
                        record["name"] = str(getattr(data, "m_Name", "") or "")
                    except Exception as exc:
                        record["read_error"] = str(exc)[:180]
                entry["objects"].append(record)
                if any(word in record.get("name", "").lower() for word in KEYWORDS):
                    candidates.append({"file": relative, **record})
            entry["types"] = dict(types)
        except Exception as exc:
            entry["error"] = f"{type(exc).__name__}: {exc}"[:400]
        results.append(entry)
        print(relative, entry["types"] or entry["error"])
    output = Path("workspace")
    output.mkdir(exist_ok=True)
    (output / "unity-assets.json").write_text(json.dumps(results, indent=2), encoding="utf-8")
    (output / "ui-candidates.json").write_text(json.dumps(candidates, indent=2), encoding="utf-8")
    print(f"Scanned {len(results)} files, found {len(candidates)} named candidates.")

if __name__ == "__main__":
    main()
