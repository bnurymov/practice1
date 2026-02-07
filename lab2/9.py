n = int(input())
nums = list(map(int, input().split()))
number = sorted(nums)
for i in nums:
    if(i == number[n - 1]):
        print(number[0], end = " ")
    else:
        print(i, end = " ")