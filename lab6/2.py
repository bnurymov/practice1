def myfunc(x):
    return(x % 2 == 0)

n = int(input())
num = list(map(int, input().split()))
func = filter(myfunc, (num))
print(len(list(func)))