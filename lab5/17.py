import re

x = input()

dates = re.findall(r"\d{2}/\d{2}/\d{4}", x)

print(len(dates))