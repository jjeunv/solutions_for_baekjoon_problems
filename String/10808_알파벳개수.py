cmd = list(input())

for i in range(ord("a"), ord("z") + 1):
    print(cmd.count(chr(i)), end=" ")
