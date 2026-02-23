n = int(input())
a = True
if(n >= 2):
    print(2, end = " ")
for i in range(3, n + 1):
    for j in range(2, i):
        if(i % j == 0):
            a = False
    if(a):
        print(i, end = " ")
    a = True
