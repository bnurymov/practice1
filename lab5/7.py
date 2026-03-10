import re
text = input()
subtext1 = input()
subtext2 = input()
n = re.sub(subtext1, subtext2, text)
print(n)