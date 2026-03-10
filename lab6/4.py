n = int(input())
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
x = zip(num1, num2)
x = list(x)
sum = 0
for i in range(n):
    sum += x[i][0] * x[i][1]
print(sum)
