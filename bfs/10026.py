# 백준 10026번 '적록색약'

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(a, b, color):
    q = deque()
    q.append((a, b))
    visited[a][b] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if not visited[nx][ny] and graph[nx][ny] == color:
                q.append((nx, ny))
                visited[nx][ny] = 1

normal_count = 0
mutant_count = 0

visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            BFS(i, j, graph[i][j])
            normal_count += 1

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            BFS(i, j, graph[i][j])
            mutant_count += 1

print(normal_count, mutant_count)
