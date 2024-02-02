n = int(input())

flag = 0
for num in range(1, n + 1):
    if num + sum(list(map(int, str(num)))) == n:
        flag = 1
        print(num)
        break

if flag == 0:
    print(0)
