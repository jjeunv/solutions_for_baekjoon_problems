n = list(map(int, input().split()))

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if n[0] * i + n[1] * j == n[2] and n[3] * i + n[4] * j == n[5]:
            print(i, j)
            break
