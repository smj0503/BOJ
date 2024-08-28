# 백준 3187번 '양치기 꿍'

from collections import deque

n, m = map(int, input().split())

field = []
wolf_total = 0    # 늑대 total count
sheep_total = 0   # 양 total count

for _ in range(n):
    field.append(list(input()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(graph, a, b):
    q = deque()
    q.append((a, b))

    global wolf_total, sheep_total
    wolf = 0   # 늑대
    sheep = 0  # 양

    if graph[a][b] == 'v':
        wolf += 1
    elif graph[a][b] == 'k':
        sheep += 1

    graph[a][b] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or graph[nx][ny] == '#':
                continue

            if graph[nx][ny] == 'v':
                graph[nx][ny] = 0
                q.append((nx, ny))
                wolf += 1
            elif graph[nx][ny] == 'k':
                graph[nx][ny] = 0
                q.append((nx, ny))
                sheep += 1
            elif graph[nx][ny] == '.':
                graph[nx][ny] = 0
                q.append((nx, ny))

    if sheep > wolf:
        wolf = 0
    else:
        sheep = 0

    wolf_total += wolf
    sheep_total += sheep

for i in range(n):
    for j in range(m):
        if field[i][j] != '#' and field[i][j] != 0:
            BFS(field, i, j)

print(sheep_total, wolf_total)
