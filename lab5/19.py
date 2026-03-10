import re

x = input()

pattern = re.compile(r"\b\w+\b")

words = pattern.findall(x)

print(len(words))