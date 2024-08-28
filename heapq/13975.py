# 백준 13975 '파일 합치기 3'

import sys
import heapq
input = sys.stdin.readline

T = int(input())
results = []

for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    ans = 0

    heapq.heapify(files)
    while len(files) > 1:
        a = heapq.heappop(files)
        b = heapq.heappop(files)
        ans += (a + b)
        heapq.heappush(files, a + b)
    results.append(ans)

for r in results:
    print(r)
