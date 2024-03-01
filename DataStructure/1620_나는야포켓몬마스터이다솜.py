import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())

book = dict()
order = dict()

for i in range(1, n + 1):
    cmd = input().strip()
    book[cmd] = i
    order[i] = cmd


for _ in range(m):
    cmd = input().strip()
    if cmd[0].isupper():
        print(book[cmd])
    else:
        print(order[int(cmd)])
