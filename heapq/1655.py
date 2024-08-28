# 백준 1655 '가운데를 말해요'

import sys
import heapq
input = sys.stdin.readline

N = int(input())

left_heap = []   # 최대 힙
right_heap = []  # 최소 힙
mid_values =[]

for _ in range(N):
    num = int(input())

    # leftHeap과 rightHeap의 개수의 균형을 맞춰 준다.
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)

    if right_heap and right_heap[0] < - left_heap[0]:
        temp_left = heapq.heappop(left_heap)
        temp_right = heapq.heappop(right_heap)

        heapq.heappush(left_heap, -temp_right)
        heapq.heappush(right_heap, -temp_left)

    mid_values.append(-left_heap[0])

for mid in mid_values:
    print(mid)
