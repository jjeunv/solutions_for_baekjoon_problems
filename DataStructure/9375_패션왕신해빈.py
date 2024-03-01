for _ in range(int(input())):
    n = int(input())
    clothes = dict()

    for _ in range(n):
        name, t = input().split()
        if not t in clothes.keys():
            clothes[t] = [name]
        else:
            clothes[t].append(name)

    ans = 1
    for i in clothes.values():
        ans *= len(i) + 1

    print(ans - 1)
