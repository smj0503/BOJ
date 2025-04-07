# BOJ 1520 '내리막 길'

from collections import deque
import sys
input = sys.stdin.readline

# m: x, n: y
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
visited = [[0] * n for _ in range(m)]
cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(a, b):
    global cnt
    if a == m-1 and b == n-1:
        cnt += 1
        return

    q = deque()
    q.append([a, b])
    visited[a][b] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[x][y] > graph[nx][ny] and not visited[nx][ny]:
                q.append([nx, ny])
                visited[nx][ny] = 1
                dfs(nx, ny)
                q.pop()
                visited[nx][ny] = 0

print(cnt)
