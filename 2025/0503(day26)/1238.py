# BOJ 1238

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))

def dijkstra(start):
    distance = [INF] * (n+1)
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

    return distance

required_time = dijkstra(x)
for i in range(1, n+1):
    if i != x:
        temp = dijkstra(i)
        required_time[i] += temp[x]

required_time.pop(0)
print(max(required_time))
