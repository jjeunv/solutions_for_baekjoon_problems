from itertools import product
import sys

n, m = map(int, input().split())

dna_list = [list(input()) for _ in range(n)]
dna = ["A", "C", "G", "T"]
ans = 0
cor = []

for i in range(m):
    sum = n + 1
    ans_dna = []
    for j in dna:
        cnt = 0
        for k in dna_list:
            if j != k[i]:
                cnt += 1
        if cnt < sum:
            sum = cnt
            ans_dna = j
    ans += sum
    cor.append(ans_dna)


print("".join(cor))
print(ans)
