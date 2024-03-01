cmd = input()

for i in cmd:
    if i.isupper():
        print(chr(ord("A") + (ord(i) + 13 - ord("A")) % 26), end="")
    elif i.islower():
        print(chr(ord("a") + (ord(i) - 13 - ord("a")) % 26), end="")
    else:
        print(i, end="")
