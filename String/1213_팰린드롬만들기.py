from itertools import permutations

name = list(input())
ans = []
for i in permutations(name, len(name)):
    if i == i[::-1]:
        ans.append(i)

ans.sort()
if len(ans) == 0:
    print("I'm Sorry Hansoo")
else:
    print("".join(ans[0]))
