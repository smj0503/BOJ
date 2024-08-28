# 백준 2075 'N번째 큰 수'

import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    numbers = list(map(int, input().split()))
    if not heap:
        for num in numbers:
            heapq.heappush(heap, num)
    else:
        for num in numbers:
            if heap[0] < num:
                heapq.heappush(heap, num)
                heapq.heappop(heap)

print(heap[0])
