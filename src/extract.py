import json
import sys
from pathlib import Path
import shutil
import argparse

SCRIPT_DIR = Path(__file__).parent.resolve()
DATA_DIR = SCRIPT_DIR.parent / 'data'

parser = argparse.ArgumentParser(
    description = "A program to convert Wuthering Waves .json Spine file to Spine Atlas and Skeleton files.",
    epilog = "Examples:\n"
             "    python extract.py -f c_suoming_01\n"
             "    python extract.py -a ../data/sc0304\n\n"
             "Default directory for .json files is {DATA_DIR}",
    formatter_class = argparse.RawDescriptionHelpFormatter
)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-f", "--file", help="Path to the JSON file to extract")
group.add_argument("-a", "--all-files", help="Extract all JSON files in the given directory")
args = parser.parse_args()

if args.file:
    file_path = Path(args.file).with_suffix('.json')
    files = [file_path] if file_path.is_file() else [DATA_DIR / file_path]
else:
    files = Path(args.all_files).rglob('*.json')

extracted = []
textures_dirs = set()

# def write_atlas(atlas_path: Path, old_png: str,new_png: str,
#                 raw_data, encoding: str = 'utf-8'):
#     atlas_content = atlas_path.read_text(encoding=encoding)
#     atlas_content_new = atlas_content.replace(old_png, new_png)
#     atlas_path.write_text(atlas_content_new, encoding=encoding)

for json_file in files:
    if not json_file.is_file():
        print(f"File not found: {json_file}")
        continue

    with open(json_file, 'r', encoding='utf-8') as f:
        json_data = json.load(f)
        
    # Convert single json object to list
    if isinstance(json_data, dict):
        json_data = [json_data]

    output_filename = json_file.with_suffix('')

    for item in json_data:
        item_type = item.get('Type', "invalid")
        raw_data = item.get('Properties', {}).get('rawData')

        if item_type == 'SpineAtlasAsset' or (isinstance(raw_data, str) and not item_type):
            atlas_path = output_filename.with_suffix('.atlas')
            atlas_path.write_text(raw_data.replace('\\n', '\n'), encoding='utf-8')
            extracted.append(atlas_path.name)

        elif item_type == 'SpineSkeletonDataAsset' or (isinstance(raw_data, list) and not item_type):
            skel_path = output_filename.with_suffix('.skel')
            skel_path.write_bytes(bytearray(raw_data))
            extracted.append(skel_path.name)

        elif item_type == 'invalid':
            continue

    textures_dir = json_file.parent / 'Textures'
    if textures_dir not in textures_dirs:
        for image in textures_dir.glob('*.png'):
            shutil.move(image, json_file.parent)
        textures_dirs.add(textures_dir)

# skel_files = [Path(f) for f in extracted if f.suffix == '.skel']
# for skel in skel_files:
#     if not skel.suffix('.atlas'):
#         atlas_path = output_base.with_suffix('.atlas')
#         shutil

if extracted: print(f"Extraction complete: {', '.join(extracted)}")
else: print("No Spine atlas or skeleton data found to extract.")