n, k = map(int, input().split())
n = int(n)

ans = 0

for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            if k in (h // 10, h % 10, m // 10, m % 10, s // 10, s % 10):
                ans += 1
print(ans)
