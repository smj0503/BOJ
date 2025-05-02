# BOJ 13549 '숨바꼭질 3'

import heapq
INF = int(1e9)
MAX = 10 ** 5

n, k = map(int, input().split())
distance = [INF] * (MAX + 1)

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, cur = heapq.heappop(q)
        if distance[cur] < dist:
            continue
        for x in (cur+1, cur-1, cur*2):
            if 0 <= x <= MAX:
                cost = dist
                if x != cur*2:
                    cost += 1
                if cost < distance[x]:
                    distance[x] = cost
                    heapq.heappush(q, (cost, x))

dijkstra(n)
print(distance[k])
