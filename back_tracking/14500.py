# BOJ 14500 '테트로미노'

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

visited = [[False for _ in range(M)] for _ in range(N)]
max_value = 0

def dfs(x, y, cnt, value):
    global max_value
    if cnt == 4:
        max_value = max(max_value, value)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, cnt + 1, value + graph[nx][ny])
            visited[nx][ny] = False

# ㅏ, ㅓ, ㅗ, ㅜ 모양 탐색 함수 (dfs로는 탐색 불가)
# 탐색 방법
# 시작점 기준으로 상,하,좌,우 좌표에 해당하는 값을 배열에 담고,
# 해당 배열에서 최소값을 제외하고 나머지 값들을 모두 더하면 된다.
def find_t(x, y):
    global max_value
    arr = []

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            arr.append(graph[nx][ny])

    # 사방이 모두 탐색 가능한 경우, 최솟값을 제외한 값들을 모두 더해준다
    if len(arr) == 4:
        arr.sort(reverse=True)
        arr.pop()
        max_value = max(max_value, sum(arr) + graph[x][y])
    # 사방이 모두 탐색 불가능한 경우(3방향만), 값들을 모두 더해준다.
    elif len(arr) == 3:
        max_value = max(max_value, sum(arr) + graph[x][y])

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, graph[i][j])
        find_t(i, j)
        visited[i][j] = False

print(max_value)
