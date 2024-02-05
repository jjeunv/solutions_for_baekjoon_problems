from itertools import permutations
import sys

input = sys.stdin.readline

num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

n = int(input())

answer = [list(input().split()) for _ in range(n)]


def check(a, b):
    strike, ball = 0, 0
    for i in range(3):
        for j in range(3):
            if a[i] == b[j]:
                if i == j:
                    strike += 1
                else:
                    ball += 1
    return str(strike), str(ball)


ans = 0

for i in permutations(num, 3):
    curNum = "".join(i)
    cnt = 0
    for ansNum, strike, ball in answer:
        s, b = check(curNum, str(ansNum))
        if strike == s and ball == b:
            cnt += 1
    if cnt == n:
        ans += 1

print(ans)
