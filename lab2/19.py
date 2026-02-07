n = int(input())

total = {}

for i in range(n):
    s, k = input().split()
    k = int(k)
    total[s] = total.get(s, 0) + k

for name in sorted(total):
    print(name, total[name])
