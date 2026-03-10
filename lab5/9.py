import re
text = input()
n = re.findall(r"\w{cat, dog}", text)
print(len(n))