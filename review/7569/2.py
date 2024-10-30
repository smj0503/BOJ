# BOJ 7569 '토마토'

import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())

box = []
for _ in range(H):
    line = []
    for _ in range(N):
        line.append(list(map(int, input().split())))
    box.append(line)

q = deque()
for k in range(H):
    for i in range(N):
        for j in range(M):
            if box[k][i][j] == 1:
                q.append([i, j, k])

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def bfs():
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < N and 0 <= ny < M and 0 <= nz < H and box[nz][nx][ny] == 0:
                box[nz][nx][ny] = box[z][x][y] + 1
                q.append([nx, ny, nz])

bfs()

ans = 0
for b in box:
    for line in b:
        for tomato in line:
            if tomato == 0:
                print(-1)
                exit(0)
        ans = max(ans, max(line))

print(ans - 1)
