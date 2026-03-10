n = input()
num = list(map(int, input().split()))
anylist = list()
for i in num:
    if i < 0:
        anylist.append(False)
    else:
        anylist.append(True)
x = all(anylist)
if x:
    print("Yes")
else:
    print("No")