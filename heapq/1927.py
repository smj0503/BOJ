# 백준 1927 '최소 힙'

import sys
import heapq
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

heap = []

for x in arr:
    if x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, x)
