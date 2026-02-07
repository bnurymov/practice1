n = int(input())
m = 1
nums = list(map(int, input().split()))
for i in range(n - 1):
    if(nums[i + 1] % nums[i] == 0):
        print("Yes")
        m = 0
        break
if(m == 1):
    print("No")
    
    
