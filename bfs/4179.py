# 백준 4179번 '불!'
# bfs (시작점이 두 종류)
# [접근 포인트]
# 1. 지훈이의 좌표, 불의 좌표, 지훈이의 이동 시간(시작점으로 부터의 거리), 불의 이동 시간(시작점으로 부터의 거리)을 따로 기록해준다.
# 2. 우선 불에 대해 bfs를 실행하여 불이 번지는 시간을 먼저 구한다.
# 3. 다음으론 지훈이가 도망갈 수 있는 시간을 bfs로 구한다.
# 4-1. 지훈이가 이동할 칸에 불이 붙지 않았거나,
# 4-2. 불이 붙었더라도 지훈이가 해당 칸으로 이동하는데 걸린 시간보다 불이 이동한 시간이 더 크면 해당 칸으로 이동할 수 있다.

import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
maze = [list(input().rstrip()) for _ in range(R)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 지훈이의 위치(시작점)
jihoon = deque()
# 불의 위치(시작점)
fire = deque()

# 지훈이의 이동 시간
j_time = [[0] * C for _ in range(R)]
# 불의 이동 시간
f_time = [[0] * C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if maze[i][j] == "J":
            # 지훈이의 위치 저장
            jihoon.append([i, j])
            # 지훈이의 이동 시간 초기화
            j_time[i][j] = 1
        if maze[i][j] == "F":
            # 불의 위치 저장
            fire.append([i, j])
            # 불의 이동 시간 초기화
            f_time[i][j] = 1

def bfs():
    while fire:
        x, y = fire.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= R or ny < 0 or ny >= C: continue

            # 이동할 칸(nx, ny)이 벽이 아니고,
            # 해당 칸의 이동 시간이 0인 경우, 즉 아직 탐색 하지 않은 칸일 경우
            if maze[nx][ny] != "#" and not f_time[nx][ny]:
                # 이동할 칸(nx, ny)의 값을 현재 칸(x, y)의 이동 시간에 +1 한 값으로 설정 하고
                # fire 큐에 해당 칸의 좌표 기록
                f_time[nx][ny] = f_time[x][y] + 1
                fire.append([nx, ny])

    while jihoon:
        x, y = jihoon.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 이동할 칸이 미로의 범위를 벗어날 경우,
            # 즉 지훈이가 탈출에 성공 했을 경우, 현재 칸의 이동 시간을 반환
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                return j_time[x][y]
            if maze[nx][ny] == '#' or j_time[nx][ny]:
                continue

            # 이동할 칸(nx, ny)에 대한 불의 이동 시간이 없거나,
            # (= 불이 번지지 않은 칸일 경우)
            # 혹은 이동할 칸에 대한 불의 이동 시간이 현재 칸에 대한 지훈이의 이동 시간에 +1 한 값보다 클 경우,
            # (= 해당 칸으로 불이 번지긴 하지만 지훈이 보다는 늦게 도달)
            if not f_time[nx][ny] or f_time[nx][ny] > j_time[x][y] + 1:
                # 이동할 칸(nx, ny)의 값을 현재 칸(x, y)의 이동 시간에 +1 한 값으로 설정 하고
                # jihoon 큐에 해당 칸의 좌표 기록
                j_time[nx][ny] = j_time[x][y] + 1
                jihoon.append([nx, ny])

    return 'IMPOSSIBLE'

print(bfs())
