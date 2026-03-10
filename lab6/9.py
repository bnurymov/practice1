n = int(input())
keys = input().split()
values = input().split()
word = input()
a = True
x = list(zip(keys, values))
for i in range(n):
    if word == x[i][0]:
        print(x[i][1])
        a = False
if a:
    print("Not found")