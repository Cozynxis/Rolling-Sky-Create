# Test plan

1. Preserve an untouched original installation and verify it launches on Windows.
2. Copy the installation into a disposable test directory.
3. Identify Unity version and asset format before writing any assets.
4. Change only one visual asset in the test copy, with a reversible backup.
5. Verify startup, menu navigation, level loading, audio, and exit.
6. Add UI modifications incrementally, retaining rollback capability.
7. Test new theme and model loading separately before merging.
8. Package a patch rather than an unlicensed complete game distribution.

**Not yet tested:** All runtime steps require a Windows test environment.
