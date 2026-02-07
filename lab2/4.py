n = int(input())
a = 0
nums = list(map(int, input().split()))
for i in nums:
    if(i > 0):
        a = a + 1

print(a)