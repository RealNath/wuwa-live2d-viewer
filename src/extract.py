import json

with open('c_luosela_01.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 1. Extract the .atlas file
# The first object contains the atlas text
atlas_raw = data[0]['Properties']['rawData']
with open('c_luosela_01.atlas', 'w', encoding='utf-8') as f:
    # If the JSON parsed the literal '\n' string, replace it with actual newlines
    f.write(atlas_raw.replace('\\n', '\n'))

# 2. Extract the .skel binary file
# The second object contains the skeleton byte array
skel_raw = data[1]['Properties']['rawData']
with open('c_luosela_01.skel', 'wb') as f:
    f.write(bytearray(skel_raw))

print("Extraction complete.")