# 백준 11279 '최대 힙'

import sys
import heapq
input = sys.stdin.readline

N = int(input())
cal = []
ans = []
for _ in range(N):
    num = int(input())
    if num == 0:
        if len(cal) == 0:
            ans.append(num)
        else:
            ans.append(heapq.heappop(cal)[1])
    else:
        heapq.heappush(cal, (-num, num))

for x in ans:
    print(x)
