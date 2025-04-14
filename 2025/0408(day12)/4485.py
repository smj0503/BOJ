# BOJ 4485 '녹색 옷 입은 애가 젤다지?'

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 1

def dijkstra():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    dist[0][0] = 0

    while q:
        cost, x, y = heapq.heappop(q)

        if x == n-1 and y == n-1:
            print(f'Problem {count}: {dist[x][y]}')
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                nc = cost + graph[nx][ny]

                if nc < dist[nx][ny]:
                    dist[nx][ny] = nc
                    heapq.heappush(q, (nc, nx, ny))

while True:
    n = int(input())
    if n == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(n)]
    dist = [[INF] * n for _ in range(n)]

    dijkstra()
    count += 1
