# BOJ 14503 '로봇 청소기'
# point : -1 % 4 = 3
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def robot(x, y, z):
    global cnt
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        # 현재 위치가 청소되어 있지 않다면(0)
        if room[x][y] == 0:
            # 청소를 하고, 청소 했다는 표시(x)를 남긴 후, cnt+1
            room[x][y] = 2
            cnt += 1

        dirty = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if room[nx][ny] == 0:
                dirty += 1

        if dirty == 0:
            nx, ny = x + dx[(z - 2) % 4], y + dy[(z - 2) % 4]
            if room[nx][ny] == 1:
                break
            else:
                q.append((nx, ny))
        else:
            z = (z - 1) % 4
            nx, ny = x + dx[z], y + dy[z]
            if room[nx][ny] == 0:
                q.append((nx, ny))
            else:
                q.append((x, y))
    print(cnt)

robot(r, c, d)
