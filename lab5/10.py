import re
text = input()
n = re.search(r"\w{cat, dog}", text)
if n:
    print("Yes")
else:
    print("No")