# BOJ 1520 '내리막 길'

# dp[x][y] : (x,y)에서 종점까지 가는 방법의 수
# 예를 들어 (0,3)의 경우, (0,4) 혹은 (1,3)으로 나갈 수 있다.
# (0,4), (1,3) 에서 종점까지 가는 방법의 수는 dfs(0,4), dfs(1,3)로 구할 수 있다.
# 즉, (0,3)에서 종점까지 가는 방법의 수는 dfs(0,4) + dfs(1,3)과 같다.
# 기존에 구했던 dfs값을 재활용하여 시간복잡도를 줄일 수 있는 것이다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

# 편하게 보기 위해 M,N 스왑
m, n = map(int, input().split())
n, m = m, n

graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    if (x, y) == (n-1, m-1):
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[x][y] > graph[nx][ny]:
                dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(0, 0))
