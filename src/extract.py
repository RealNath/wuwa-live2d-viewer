import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.resolve()
DATA_DIR = SCRIPT_DIR.parent / 'data'

if len(sys.argv) != 2:
    print("Use `python extract.py <JSON_NAME>`")
    sys.exit(1)

input_arg = Path(sys.argv[1])
base_name = input_arg.with_suffix('') if input_arg.suffix == '.json' else input_arg

if input_arg.is_file():
    json_path = input_arg
    output_base = base_name
elif (DATA_DIR / f'{base_name}.json').is_file():
    json_path = DATA_DIR / f'{base_name}.json'
    output_base = DATA_DIR / base_name
elif (DATA_DIR / input_arg).is_file():
    json_path = DATA_DIR / input_arg
    output_base = DATA_DIR / base_name
else:
    raise FileNotFoundError(f"File '{sys.argv[1]}' not found in data directory or path.")

with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Convert single JSON object (if not a list) to list of objects
if isinstance(data, dict): data = [data]

extracted = []
for item in data:
    item_type = item.get('Type')
    raw_data = item.get('Properties', {}).get('rawData')

    if item_type == 'SpineAtlasAsset' or (isinstance(raw_data, str) and not item_type):
        atlas_path = output_base.with_suffix('.atlas')
        with open(atlas_path, 'w', encoding='utf-8') as f:
            f.write(raw_data.replace('\\n', '\n'))
        extracted.append(atlas_path.name)

    elif item_type == 'SpineSkeletonDataAsset' or (isinstance(raw_data, list) and not item_type):
        skel_path = output_base.with_suffix('.skel')
        with open(skel_path, 'wb') as f:
            f.write(bytearray(raw_data))
        extracted.append(skel_path.name)

if extracted: print(f"Extraction complete: {', '.join(extracted)}")
else: print("No Spine atlas or skeleton data found to extract.")