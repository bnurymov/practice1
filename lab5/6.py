import re
text = input()
n = re.findall(r"\b[\w.-]+@[\w.-]+\.\w+\b", text)
if(len(n)):
    print(n[0])
else:
    print("No email")