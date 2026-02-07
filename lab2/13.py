n = int(input())
m = 1
for i in range(2, n - 1):
    if(n % i == 0):
        print("No")
        m = 0
        break
if(m == 1):
    print("Yes")
    
    
