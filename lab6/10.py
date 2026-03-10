n = int(input())
nums = list(map(int, input().split()))
a = 0
for i in nums:
    if i != 0:
        a += 1
print(a)
