import sys
from collections import deque
input = sys.stdin.readline

# 전체 그래프의 너비 = n * m
N, M = map(int, input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[False for _ in range(M)] for _ in range(N)]

# graph = bfs를 실시할 그래프
def BFS(graph, visited, start):
  q = deque([start])
  visited[start[0]][start[1]] = True
  count = 1 # 칸의 개수. 즉, 너비

  while q:
    x, y = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      # 범위(n, m)를 벗어나는 경우는 pass
      if nx < 0 or nx >= N or ny < 0 or ny >= M: continue
      if visited[nx][ny] or graph[nx][ny] == 0: continue

      q.append((nx, ny))
      visited[nx][ny] = True
      count += 1

  return count
