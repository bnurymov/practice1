import json
n = True
j3 = list()
text1 = input()
text2 = input()
j1 = json.loads(text1)
j2 = json.loads(text2)
for i in j1:
    j3.append(i)
    print(j3[0], end = "")
    print("123")
    print(i, "123")