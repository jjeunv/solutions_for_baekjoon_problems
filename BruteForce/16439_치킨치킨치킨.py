import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

preference = [list(map(int, input().split())) for _ in range(n)]

chicken = [i for i in range(1, m + 1)]

ans = 0
for f, s, t in combinations(chicken, 3):
    sum = 0
    for p in preference:
        sum += max(p[f - 1], p[s - 1], p[t - 1])
    ans = max(ans, sum)

print(ans)
