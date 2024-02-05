from itertools import permutations

n = int(input())
k = int(input())
card = [(input()) for _ in range(n)]

card_list = permutations(card, k)

select = ["".join(i) for i in permutations(card, k)]
print(len(set(select)))
