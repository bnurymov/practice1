import re
text = input()
pattern = input()
n = re.split(pattern, text)
for i in range(len(n)):
    if(i != len(n) - 1):
        print(n[i], end = ",")
    else:
        print(n[i])