n = int(input())
a = 0
while(n != 2):
    if(n % 2 == 0):
        n = n // 2
    else:
        a = 1
        break
if(a == 0):
    print("YES")
else:
    print("NO")