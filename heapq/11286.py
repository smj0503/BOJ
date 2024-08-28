# 백준 11286 '절댓값 힙'

import sys
import heapq
input = sys.stdin.readline

N = int(input())

plus = []
minus = []
result = []

for _ in range(N):
    num = int(input())
    if num > 0:
        heapq.heappush(plus, num)
    elif num < 0:
        heapq.heappush(minus, -num)
    else:
        if plus and minus:
            if plus[0] > minus[0]:
                result.append(-heapq.heappop(minus))
            elif plus[0] < minus[0]:
                result.append(heapq.heappop(plus))
            else:
                result.append(-heapq.heappop(minus))
        elif plus and not minus:
            result.append(heapq.heappop(plus))
        elif not plus and minus:
            result.append(-heapq.heappop(minus))
        else:
            result.append(0)

for r in result:
    print(r)
