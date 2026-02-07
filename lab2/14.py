n = int(input())
a = list(map(int, input().split()))

cnt = {}
for x in a:
    cnt[x] = cnt.get(x, 0) + 1

best_val = None
best_cnt = -1

for x, c in cnt.items():
    if c > best_cnt or (c == best_cnt and (best_val is None or x < best_val)):
        best_cnt = c
        best_val = x

print(best_val)


