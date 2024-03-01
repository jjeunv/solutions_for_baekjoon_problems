import sys

input = sys.stdin.readline

n = int(input())
pattern = list(input().strip())
file = [list(input().strip()) for _ in range(n)]

idx = pattern.index("*")
front = pattern[:idx]
back = pattern[:idx:-1]

for i in file:
    if len(i) < len(front) or len(i) < len(back) or len(i) < len(pattern) - 1:
        print("NE")
        continue
    if i[: len(front)] != front or i[len(i) - 1 : len(i) - 1 - len(back) : -1] != back:
        print("NE")
        continue
    print("DA")
