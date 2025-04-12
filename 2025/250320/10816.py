# BOJ 10816 '숫자 카드 2'

import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
hash_table = {}

for c in cards:
    if c in hash_table:
        hash_table[c] += 1
    else:
        hash_table[c] = 1

M = int(input())
targets = list(map(int, input().split()))

answer = []
for t in targets:
    if t in hash_table:
        answer.append(hash_table[t])
    else:
        answer.append(0)

print(*answer)
