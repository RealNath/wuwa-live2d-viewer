## Wuthering Waves Spine 2D (Live2D) viewer

This is a prototype of showing Live2D animation (Spine 2D) of Wuthering Waves stuff (e.g splash art). You can get the asset files (json and sprite png) with FModel. Then run extract.py to extract the skel and atlas files. After that, run index.html to view the animation.

### How to Run

1. Get the game files from FModel, put it in `src`.  
   For example, Lucilla's splash art: `Client/Content/Aki/UI/UIResources/UiLuckdraw/Spine/Character/C_LuoSeLa_01`  
   Extract both the SpineAtlasAsset file, and the sprite .png in `Textures` folder.
2. Edit and run `python3 extract.py` to extract the skel and atlas files.
3. Run `python -m http.server 8000` and open `http://localhost:8000` in your browser.