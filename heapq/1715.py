# 백준 1715 '카드 정렬하기'

import sys
import heapq
input = sys.stdin.readline

N = int(input())
deck = []
ans = 0

for _ in range(N):
    heapq.heappush(deck, int(input()))

while len(deck) > 1:
    a = heapq.heappop(deck)
    b = heapq.heappop(deck)
    ans += (a + b)
    heapq.heappush(deck, a + b)

print(ans)
