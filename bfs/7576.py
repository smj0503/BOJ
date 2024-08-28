# 백준 7576번 '토마토'
# bfs (시작점이 여러개)
# [접근 포인트]
# 1. 익은 토마토가 여러개일수 있으므로, 모든 익은 토마토의 좌표를 큐에 담아준다.
# 2. 그 후 각 좌표에 대해 순차적으로 bfs를 실행한다.

import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
box = []
ans = 0

for _ in range(N):
  box.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 익은 토마토들의 좌표를 큐에 담아준다
q = deque([])
for i in range(N):
  for j in range(M):
    if box[i][j] == 1:
      q.append([i, j])

def BFS():
  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
        box[nx][ny] = box[x][y] + 1
        q.append([nx, ny])

BFS()

for line in box:
  for tomato in line:
    if tomato == 0:
      print(-1)
      exit(0)
  ans = max(ans, max(line))

print(ans - 1)
