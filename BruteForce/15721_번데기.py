a = int(input())
t = int(input())
n = str(input())

first = "0101"
second = "00"
third = "11"

cnt, flag, num = 0, 0, 0

while True:
    cmd = first + second + third
    for i in cmd:
        if i == n:
            cnt += 1
        if cnt == t:
            flag = 1
            break
        num += 1
        if num >= a:
            num = 0
    if flag == 1:
        break
    second += "0"
    third += "1"

print(num)
