n = int(input())
nums = list(map(int, input().split()))
numbers = sorted(set(nums))
for i in numbers:
    print(i, end = " ")