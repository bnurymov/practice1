import re
text = input()
subtext = input()
n = re.findall(subtext, text)
print(len(n))