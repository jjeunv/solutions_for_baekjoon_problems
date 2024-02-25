charge = list(map(int, input().split()))

vert = [0] * 101

for _ in range(3):
    arrive, leave = map(int, input().split())
    for i in range(arrive, leave):
        vert[i] += 1

ans = 0

for i in vert:
    if i == 0:
        continue
    ans += charge[i - 1] * i

print(ans)
