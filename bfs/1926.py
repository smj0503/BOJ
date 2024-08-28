# 백준 1926번 '그림'
# bfs (시작점이 여러개)
# [접근 포인트]
# 이중 for문으로 그래프를 돌며 그림의 시작점이 될 수 있는 곳(값이 1이고, 아직 방문하지 않은. 즉 visited가 false인 지점)에서 bfs 실행.

from collections import deque

# 전체 그래프의 너비 = n * m
n, m = map(int, input().split())
graph = []

for i in range(n):
  graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# graph = bfs를 실시할 그래프 / (a, b) = 탐색을 시작하는 지점
def bfs(graph, a, b):
  queue = deque()

  queue.append((a, b))
  graph[a][b] = 0
  count = 1

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        queue.append((nx, ny))
        count += 1

  return count

paint = []

for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      paint.append(bfs(graph, i, j))


if len(paint) == 0:
  print(len(paint))
  print(0)
else:
  print(len(paint))
  print(max(paint))
