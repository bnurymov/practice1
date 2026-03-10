import re
text = input()
n = re.search("^[A-z].*[0-9]$", text)
if n:
    print("Yes")
else:
    print("No")