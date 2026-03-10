import json
n = True
text1 = input()
text2 = input()
j1 = json.loads(text1)
j2 = json.loads(text2)
for i in j1:
    if(j1[i] != j2[i]):
        if not isinstance(j1[i], dict):
            print(i, ":",j1[i], "->", j2[i])
            n = False
            break
        else:
            for j in j1[i]:
                if(j1[i][j] != j2[i][j]):
                    print(i, end = ".")
                    print(j, ":", j1[i][j], "->", j2[i][j])
                    n = False
                    break
if(n):
    print("No differences")