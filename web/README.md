# Rolling Sky Create — Web Engine

This is the first animated menu prototype for Rolling Sky Create.

## Preview locally

The menu uses Three.js as an ES module from esm.sh, so an internet connection is required.

From the repository root:

```powershell
py -m http.server 8000 -d web
```

Open http://localhost:8000 in a browser.

## Current features

- Animated 3D runway, obstacles, rotating ball and starfield
- Responsive glass-style menu
- Play, Level Editor and Settings buttons
- Settings for motion and render resolution
- Escape and outside-click to close modal, basic focus management

## Not yet implemented

- Gameplay, playable levels and level editor
- Unity asset conversion/import
- Music and sound
- Save data and accounts

This version uses original procedural geometry and materials, **not** converted copyrighted Unity assets. Existing extracted assets require format and usage-rights review before integration.
