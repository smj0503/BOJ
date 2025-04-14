# BOJ 10816

import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
target = list(map(int, input().split()))

counts = {}
for card in cards:
    if card not in counts:
        counts[card] = 1
    else:
        counts[card] += 1

for target in target:
    if target in counts:
        print(counts[target], end=' ')
    else:
        print(0, end=' ')
