# 백준 2178번 '미로 탐색'
# bfs (거리 측정)
# [접근 포인트]
# bfs를 실행하면서 미로의 각 칸에 시작점으로 부터의 거리를 기록

from collections import deque

N, M = map(int, input().split())

graph = []

for _ in range(N):
  graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
        queue.append((nx, ny))
        graph[nx][ny] = graph[x][y] + 1

  return graph[N-1][M-1]

print(bfs(0, 0))
