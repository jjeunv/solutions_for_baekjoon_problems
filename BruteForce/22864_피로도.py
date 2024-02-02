a, b, c, m = map(int, input().split())

ans = 0
t = 0
for _ in range(24):
    if a > m:
        break
    if t + a <= m:
        t += a
        ans += b
    else:
        t -= c
        if t < 0:
            t = 0

print(ans)
