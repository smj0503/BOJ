# 백준 2667번 '단지 번호 붙이기'
# bfs

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def BFS(graph, a, b):
    q = deque()

    q.append((a, b))
    graph[a][b] = 0
    count = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                count += 1

    return count

block = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            block.append(BFS(graph, i, j))

block.sort()
print(len(block))

for c in block:
    print(c)
