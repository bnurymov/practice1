n = int(input())
nums = list(map(int, input().split()))
a = sorted(nums, reverse = True)
b = a[0]
for i in range(n):
    if(nums[i] == b):
        print(i + 1)
        break