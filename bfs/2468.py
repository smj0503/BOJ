# 백준 2468번 '안전 영역'

from collections import deque

N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

max_height = max(map(max, graph))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(a, b, rain):
    q = deque()
    q.append((a, b))
    visited[a][b] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] == 1 or graph[nx][ny] <= rain:
                continue
            q.append((nx, ny))
            visited[nx][ny] = 1

result = 0

for i in range(max_height):
    count = 0
    visited = [[0] * N for _ in range(N)]
    for j in range(N):
        for k in range(N):
            if graph[j][k] > i and visited[j][k] == 0:
                BFS(j, k, i)
                count += 1
    result = max(result, count)

print(result)
