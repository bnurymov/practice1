import re
text = input()
subtext = input()
n = re.search(subtext, text)
if n:
    print("Yes")
else:
    print("No")