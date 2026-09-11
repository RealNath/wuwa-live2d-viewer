import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.resolve()
DATA_DIR = SCRIPT_DIR.parent / 'data'

if len(sys.argv) == 2:
    if sys.argv[1].endswith('.json'): JSON_NAME = sys.argv[1][:-5]
    else: JSON_NAME = sys.argv[1]
    
    if not (DATA_DIR / f'{JSON_NAME}.json').exists():
        raise FileNotFoundError(f"File '{JSON_NAME}.json' not found in the data directory.")
else:
    print("Use `python extract.py <JSON_NAME>` (just directly mention the json file name, no need for paths).")
    sys.exit(1)


with open(DATA_DIR / f'{JSON_NAME}.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 1. Extract .atlas file
# First object contains the atlas text
atlas_raw = data[0]['Properties']['rawData']
with open(DATA_DIR / f'{JSON_NAME}.atlas', 'w', encoding='utf-8') as f:
    # If the JSON parsed the literal '\n' string, replace it with actual newlines
    f.write(atlas_raw.replace('\\n', '\n'))

# 2. Extract .skel binary file
# Second object contains the skeleton byte array
skel_raw = data[1]['Properties']['rawData']
with open(DATA_DIR / f'{JSON_NAME}.skel', 'wb') as f:
    f.write(bytearray(skel_raw))

print("Extraction complete.")