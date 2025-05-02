# BOJ 1987

r, c = map(int, input().split())
graph = [input() for _ in range(r)]
visited = [0] * 26

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

ans = 1
visited[ord(graph[0][0]) - 65] = 1

def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not visited[ord(graph[nx][ny]) - 65]:
            visited[ord(graph[nx][ny]) - 65] = 1
            dfs(nx, ny, cnt+1)
            visited[ord(graph[nx][ny]) - 65] = 0

dfs(0, 0, 1)
print(ans)
