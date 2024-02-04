from itertools import product

n, cntk = map(str, input().split())
k = list(map(str, input().split()))
ans = 0

for i in range(1, len(n) + 1):
    for j in product(k, repeat=i):
        j = "".join(j)
        j = int(j)
        if j <= int(n):
            ans = max(ans, j)

print(ans)
