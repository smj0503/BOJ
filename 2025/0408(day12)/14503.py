# BOJ 14503

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def robot(x, y, z):
    cnt = 0
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        # case1
        if room[x][y] == 0:
            room[x][y] = 2
            cnt += 1

        dirty = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if room[nx][ny] == 0:
                dirty += 1

        # case2
        if dirty == 0:
            nx, ny = x + dx[(z-2) % 4], y + dy[(z-2) % 4]
            # 2-2
            if room[nx][ny] == 1:
                break
                # 2-1
            else:
                q.append((nx, ny))
        # case3
        else:
            # 3-1
            z = (z-1) % 4
            nx, ny = x + dx[z], y + dy[z]
            # 3-2
            if room[nx][ny] == 0:
                q.append((nx, ny))
            # 여기를 놓치네!!
            else:
                q.append((x, y))

    print(cnt)

robot(r, c, d)
