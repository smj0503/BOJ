# 백준 15903 '카드 합체 놀이'

import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
deck = list(map(int, input().split()))
heapq.heapify(deck)

for _ in range(M):
    a = heapq.heappop(deck)
    b = heapq.heappop(deck)
    heapq.heappush(deck, a + b)
    heapq.heappush(deck, a + b)

print(sum(deck))
