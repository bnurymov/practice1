# Python JSON
# Convert between Python objects and JSON

import json

# Python dict to JSON string
person = {"name": "Alice", "age": 30, "languages": ["Python", "JS"]}
json_str = json.dumps(person, indent=2)
print(json_str)

# JSON string to Python dict
data = json.loads(json_str)
print(data["name"])
print(type(data))

# Write JSON to file
with open("/tmp/data.json", "w") as f:
    json.dump(person, f, indent=2)

# Read JSON from file
with open("/tmp/data.json", "r") as f:
    loaded = json.load(f)
print(loaded)
