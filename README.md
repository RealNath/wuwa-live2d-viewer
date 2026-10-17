## Wuthering Waves Spine 2D (Live2D) viewer

This is a guide on how to view the Spine (Live2D) files from Wuthering Waves (e.g splash arts). I also provide a script to extract the skel and atlas files. You can get the asset files (json and sprite png) with FModel. Then run extract.py to extract them from the json files.

### How to Run

1. Get the files from FModel, put it in the `data` folder.  
   For example, Lucilla's splash art: `Client/Content/Aki/UI/UIResources/UiLuckdraw/Spine/Character/C_LuoSeLa_01`  
   Extract both the SpineAtlasAsset file (as JSON), and the sprite .png in `Textures` folder (as Image) into `data` folder (optional: make sure they're in the same level).
2. Run `python extract.py -f <JSON_NAME>` to extract the skel and atlas files from the json file.
   * Or `python extract.py -a <DIRECTORY>` to extract from all the json files in the directory.
   * The png images will automatically move to the same directory as the json file (for SpineViewer support).
3. Download and install https://github.com/ww-rm/SpineViewer, open it, drag-and-drop the skel file into SpineViewer.
   * You can adjust the resolution and zoom (all the splash arts width are usually 2048px).
4. Right click the animation name, Export Frame/Video.