n = int(input())
if(n % 2 == 0):
    for i in range(n):
        if(i % 2 == 0):
            print(i, end = ",")
    print(n)
else:
    for i in range(n - 2):
        if(i % 2 == 0):
            print(i, end = ",")
    print(n - 1)
