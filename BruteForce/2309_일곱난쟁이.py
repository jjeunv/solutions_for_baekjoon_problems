height = [int(input()) for _ in range(9)]

height.sort()
max_sum = sum(height)

for i in range(8):
    for j in range(i + 1, 9):
        if max_sum - (height[i] + height[j]) == 100:
            for k in height:
                if k != height[i] and k != height[j]:
                    print(k)
            exit()
