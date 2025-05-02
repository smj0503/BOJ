# BOJ 1753

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e):
    x, y, w = map(int, input().split())
    graph[x].append((y, w))

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (start, 0))

    while q:
        cur, dist = heapq.heappop(q)
        if distance[cur] < dist:
            continue

        for nx, d in graph[cur]:
            cost = dist + d
            if distance[nx] > cost:
                distance[nx] = cost
                heapq.heappush(q, (nx, cost))

dijkstra(k)
for i in range(1, v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
