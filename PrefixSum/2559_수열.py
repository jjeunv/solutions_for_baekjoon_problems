import sys

input = sys.stdin.readline

n, k = map(int, input().split())

temp = list(map(int, input().split()))

sum_num = sum(temp[:k])
ans = sum_num

for i in range(1, n - k + 1):
    sum_num = sum_num - temp[i - 1] + temp[i + k - 1]
    ans = max(ans, sum_num)
print(ans)
