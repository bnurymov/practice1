n = int(input())
m = list(map(int, input().split()))

seen = set()

for x in m:
    if x in seen:
        print("No")
    else:
        print("Yes")
        seen.add(x)
