# Python RegEx

import re

text = "The rain in Spain stays mainly in the plain"

# Search for pattern
match = re.search(r"rain", text)
if match:
    print("Found:", match.group())
    print("At position:", match.start())

# Find all matches
all_ain = re.findall(r"\w*ain\w*", text)
print("Words with 'ain':", all_ain)

# Replace
result = re.sub(r"Spain", "France", text)
print(result)

# Split
parts = re.split(r"\s+", text)
print(parts[:4])

# Email validation pattern
email = "user@example.com"
pattern = r"^[\w.-]+@[\w.-]+\.\w{2,}$"
print("Valid email:", bool(re.match(pattern, email)))
