# 백준 1504 '특정한 최단 경로'

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
    graph[b].append([c, a])
v1, v2 = map(int, input().split())

def dijkstra(st, en):
    dist = [INF] * (N + 1)
    dist[st] = 0
    pq = [[0, st]]

    while pq:
        cur_cost, cur = heapq.heappop(pq)

        if dist[cur] != cur_cost:
            continue

        for nxt_cost, nxt in graph[cur]:
            if dist[nxt] > cur_cost + nxt_cost:
                dist[nxt] = cur_cost + nxt_cost
                heapq.heappush(pq, [dist[nxt], nxt])

    return dist[en]

path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

if path1 >= INF and path2 >= INF:
    print(-1)
else:
    print(min(path1, path2))
