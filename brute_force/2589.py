# BOJ 2589 '보물섬'

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input().strip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b):
    dist = [[0 for _ in range(m)] for _ in range(n)]
    q = deque()
    q.append((a, b))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # nx, ny(인덱스)가 범위(0 <= x < n, 0 <= y < m)를 벗어 나지 않고,
            # graph[nx][ny]의 값이 'W'(바다)가 아니고,
            # dist[nx][ny] == 0 일때(아직 방문하지 않은 곳일 때)
            if 0 <= nx < n and 0<= ny < m and graph[nx][ny] != 'W' and dist[nx][ny] == 0:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1

    dist[a][b] = 0
    max_dist = -1

    for i in range(n):
        for j in range(m):
            if dist[i][j] > max_dist:
                max_dist = dist[i][j]

    return max_dist

ans = -1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            ans = max(ans, bfs(i, j))

print(ans)
