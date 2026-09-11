## Wuthering Waves Spine 2D (Live2D) viewer

This is a prototype of showing Live2D animation (Spine 2D) of Wuthering Waves stuff (e.g splash art). You can get the asset files (json and sprite png) with FModel. Then run extract.py to extract the skel and atlas files. After that, run index.html to view the animation.

### How to Run

1. Get the files from FModel, put it in `data` folder.  
   For example, Lucilla's splash art: `Client/Content/Aki/UI/UIResources/UiLuckdraw/Spine/Character/C_LuoSeLa_01`  
   Extract both the SpineAtlasAsset file (as JSON), and the sprite .png in `Textures` folder (as Image) into `data` folder (make sure they're in the same level).
2. Run `python3 extract.py <JSON_NAME>` to extract the skel and atlas files.
3. Download and install https://github.com/ww-rm/SpineViewer, open it, drag-and-drop the skel file into SpineViewer.
   * You can adjust the resolution and zoom (all the splash arts width are usually 2048px).
4. Right click the animation name, Export Frame/Video.