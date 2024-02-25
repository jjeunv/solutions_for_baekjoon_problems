import sys

input = sys.stdin.readline

n, m = map(int, input().split())

icecream = [[True for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    icecream[a][b] = False
    icecream[b][a] = False

ans = 0

for i in range(1, n - 1):
    for j in range(i + 1, n):
        for k in range(j + 1, n + 1):
            if icecream[i][j] and icecream[j][k] and icecream[k][i]:
                ans += 1
print(ans)
