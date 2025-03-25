# BOJ 10816

import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))

M = int(input())
targets = list(map(int, input().split()))

counts = {}
for c in cards:
    if c in counts:
        counts[c] += 1
    else:
        counts[c] = 1

for t in targets:
    if t in counts:
        print(counts[t], end=' ')
    else:
        print(0, end=' ')
