# 백준 11000 '강의실 배정'

import sys
import heapq
input = sys.stdin.readline

N = int(input())
courses = [list(map(int, input().split())) for _ in range(N)]
courses.sort(key=lambda x : (x[0], x[1]))

heap = [courses[0][1]]
for i in range(1, N):
    if heap[0] <= courses[i][0]:
        heapq.heappop(heap)
    heapq.heappush(heap, courses[i][1])

print(len(heap))
