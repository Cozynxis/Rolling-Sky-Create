#!/usr/bin/env python3
"""Safely extract a locally owned Rolling Sky Remake ZIP and inventory it.

Usage:
  python tools/extract_and_inventory.py path/to/RollingSkyRemake-1.3.0r-Windows.zip

Does not modify or upload the original files.
"""
import hashlib
import json
import sys
import zipfile
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python tools/extract_and_inventory.py GAME.zip")
    source = Path(sys.argv[1]).resolve()
    if not source.is_file():
        raise SystemExit(f"Not found: {source}")
    destination = Path("workspace/original-game").resolve()
    destination.mkdir(parents=True, exist_ok=True)
    inventory = []
    with zipfile.ZipFile(source) as archive:
        for entry in archive.infolist():
            if entry.is_dir():
                continue
            target = (destination / entry.filename).resolve()
            if not target.is_relative_to(destination):
                raise ValueError(f"Unsafe archive path: {entry.filename}")
            target.parent.mkdir(parents=True, exist_ok=True)
            sha = hashlib.sha256()
            with archive.open(entry) as reader, target.open("wb") as writer:
                while chunk := reader.read(1024 * 1024):
                    writer.write(chunk)
                    sha.update(chunk)
            inventory.append({"path": entry.filename, "size": entry.file_size, "sha256": sha.hexdigest()})
    report = Path("workspace/inventory.json")
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text(json.dumps({"source": source.name, "files": inventory}, indent=2), encoding="utf-8")
    print(f"Extracted {len(inventory)} files to {destination}")
    print(f"Inventory saved to {report}")

if __name__ == "__main__":
    main()
