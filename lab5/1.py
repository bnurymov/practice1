import re
text = input()
n = re.search("^Hello", text)
if n:
    print("Yes")
else:
    print("No")