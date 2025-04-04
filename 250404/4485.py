# BOJ 4485 '녹색 옷 입은 애가 젤다지?'

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = 1e9

def dfs(a, b, rup):
    global ans
    if a == n-1 and b == n-1:
        ans = min(ans, rup)
        # print(ans)
        return

    q = deque()
    q.append([a, b])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append([nx, ny])
                dfs(nx, ny, rup + graph[nx][ny])
                visited[nx][ny] = 0
                q.pop()

dfs(0, 0, 0)
print(ans)
