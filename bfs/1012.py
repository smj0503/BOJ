# 백준 1012번 '유기농 배추'

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(graph, a, b):
    q = deque()

    n = len(graph)
    m = len(graph[0])

    q.append((a, b))
    graph[a][b] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))

T = int(input())
ans = []

for _ in range(T):
    N, M, P = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    count = 0
    for _ in range(P):
        a, b = map(int, input().split())
        graph[a][b] = 1

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                BFS(graph, i, j)
                count += 1

    ans.append(count)

for a in ans:
    print(a)
