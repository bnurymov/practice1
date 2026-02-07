n = int(input())
for i in range(n):
    if(2 ** i <= n):
        print(2 ** i, end = " ")
    else:
        break