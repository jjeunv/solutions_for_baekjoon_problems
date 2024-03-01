import sys

input = sys.stdin.readline

n = int(input())
pattern = input().strip().split("*")
file = [input().strip() for _ in range(n)]

front = pattern[0]
back = pattern[1]
print(front, back)
for i in file:
    print(i[: len(front)], i[len(i) - 1 : len(i) - 1 - len(back) : -1])
    if len(i) < len(front) or len(i) < len(back) or len(i) < len(pattern) - 1:
        print("NE")
        continue
    if i[: len(front)] != front or i[len(i) - 1 : len(i) - 1 - len(back) : -1] != back:
        print("NE")
        continue
    print("DA")
