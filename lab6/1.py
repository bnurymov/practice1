def myfunc(a):
    return(a ** 2)

n = int(input())
num = list(map(int, input().split()))
x = map(myfunc, num)
print(sum(x))