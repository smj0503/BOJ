# 백준 1238 '파티'

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append([w, v])

def dijkstra(st):
    d = [INF] * (N + 1)
    d[st] = 0
    pq = [(0, st)]

    while pq:
        cur_cost, cur = heapq.heappop(pq)

        if d[cur] != cur_cost:
            continue

        for nxt_cost, nxt in graph[cur]:
            if d[nxt] > cur_cost + nxt_cost:
                d[nxt] = cur_cost + nxt_cost
                heapq.heappush(pq, (d[nxt], nxt))

    return d

# total_time : X 부터 모든 노드들 까지의 소요 시간 테이블
total_time = dijkstra(X)
total_time[0] = 0

# 모든 노드(i)들로 부터 X 까지의 소요 시간 구하기
for i in range(1, N + 1):
    if i != X:
        table = dijkstra(i)
        total_time[i] += table[X]

print(max(total_time))
