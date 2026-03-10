import re
text = input()
n1 = re.findall(r"\d", text)
for i in n1:
    print(i, end = " ")