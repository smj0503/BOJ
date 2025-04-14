# BOJ 4485

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 1

def dijkstra():
    q = []
    # 비용, x좌표, y좌표
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

                # 현재의 비용이 기존 dist 배열의 값보다 작을 경우에만 업데이트
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
