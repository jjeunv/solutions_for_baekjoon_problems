ans = 0
for _ in range(int(input())):
    cmd = list(input())
    stack = []
    for i in cmd:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    if len(stack) == 0:
        ans += 1

print(ans)
