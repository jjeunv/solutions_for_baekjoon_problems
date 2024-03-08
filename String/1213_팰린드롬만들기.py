from collections import Counter

n = list(input())
name = Counter(n)
vert = [0] * 26
num = ord("A")

cnt = 0

for k, v in name.items():
    if v == 0:
        continue
    vert[ord(k) - num] += v
    if v % 2 != 0:
        cnt += 1
    if cnt >= 2:
        print("I'm Sorry Hansoo")
        exit()

front = []
back = str()

for i in range(26):
    if vert[i] % 2 != 0:
        back = chr(i + num)
    for _ in range(vert[i] // 2):
        front.append(chr(i + num))
if back != "":
    front.append(back)

if len(n) % 2 == 0:
    back = front[::-1]
else:
    back = front[-2::-1]

print("".join(front) + "".join(back))
