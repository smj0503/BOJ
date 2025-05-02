# BOJ 5972 '택배 배송'

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (start, 0))

    while q:
        cur, dist = heapq.heappop(q)
        if distance[cur] < dist:
            continue

        for nx, w in graph[cur]:
            cost = w + dist
            if distance[nx] > cost:
                distance[nx] = cost
                heapq.heappush(q, (nx, cost))

dijkstra(1)
print(distance[n])
