import sys

input = sys.stdin.readline

n = int(input())

player = [input()[0] for _ in range(n)]

first_name = set(player)

ans = []

for i in first_name:
    if player.count(i) >= 5:
        ans.append(i)

if len(ans) == 0:
    print("PREDAJA")
else:
    ans.sort()
    print("".join(ans))
