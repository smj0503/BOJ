# BOJ 1238

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

def dijkstra(start):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (start, 0))
    distance[start] = 0

    while q:
        cur, cost = heapq.heappop(q)
        if distance[cur] < cost:
            continue

        for v, w in graph[cur]:
            if distance[v] > cost + w:
                distance[v] = cost + w
                heapq.heappush(q, (v, cost + w))

    return distance

time = dijkstra(x)
time[0] = 0
answer = 0

for i in range(1, n+1):
    if i != x:
        table = dijkstra(i)
        time[i] += table[x]

print(max(time))
