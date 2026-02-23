n = int(input())
fb = list({0, 1})
if(n != 0 and n != 1 and n != 2):
    print(fb[0], end = ",")
    print(fb[1], end = ",")
    for i in range(2, n - 1):
        fb.append(fb[i - 2] + fb[i - 1])
        print(fb[i], end = ",")
    print(fb[n - 3] + fb[n - 2])
elif(n == 1):
    print(0)
elif(n == 2):
    print("0,1")