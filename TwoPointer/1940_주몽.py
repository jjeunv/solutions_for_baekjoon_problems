n = int(input())
m = int(input())
number = sorted(map(int, input().split()))

start = 0
end = n - 1
cnt = 0

while start < end:
    num = number[start] + number[end]
    if num == m:
        cnt += 1
    if num > m:
        end -= 1
    else:
        start += 1

print(cnt)
