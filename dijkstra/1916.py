# 백준 1916 '최소비용 구하기'

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([c, b])
st, en = map(int, input().split())

def dijkstra(start, end):
    dist = [INF] * (N + 1)
    dist[start] = 0
    pq = [[0, start]]

    while pq:
        cur_cost, cur = heapq.heappop(pq)

        if dist[cur] != cur_cost:
            continue

        for nxt_cost, nxt in graph[cur]:
            if dist[nxt] > cur_cost + nxt_cost:
                dist[nxt] = cur_cost + nxt_cost
                heapq.heappush(pq, [dist[nxt], nxt])

    return dist[en]

print(dijkstra(st, en))
