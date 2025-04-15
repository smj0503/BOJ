# BOJ 1987 '알파벳'

import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]

ans = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [0] * 26
visited[ord(board[0][0]) - 65] = 1

def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and not visited[ord(board[nx][ny]) - 65]:
            visited[ord(board[nx][ny]) - 65] = 1
            dfs(nx, ny, cnt + 1)
            visited[ord(board[nx][ny]) - 65] = 0
    return

dfs(0, 0, 1)
print(ans)
