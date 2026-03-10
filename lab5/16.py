import re

x = input()

m = re.search(r"Name: (.*), Age: (\d+)", x)

print(m.group(1), m.group(2))