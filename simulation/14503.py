# BOJ 14503 '로봇 청소기'

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
i, j, d = map(int, input().split())

room = []
for _ in range(N):
    room.append(list(map(int, input().split())))

# 나침반 : 북(0), 서(3), 남(2), 동(1) 순서
# (4-i) % 4
# 반시계 방향 90도 회전시 : 나침반에서 '현재 인덱스 + 1'
# 후진 시 : 나침반에서 '현재 인덱스 - 2'
nav = [[-1, 0], [0, -1], [1, 0], [0, 1]]
cnt = 0
# 방향 초기값
# cur_dir = (4 - d) % 4

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solution(x, y, z):
    global cnt
    cur_dir = (4 - z) % 4

    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        # 현재 위치가 청소되어 있지 않다면(0)
        if room[x][y] == 0:
            # 청소를 하고, 청소 했다는 표시(x)를 남긴 후, cnt+1
            room[x][y] = 'x'
            cnt += 1

        # 현재 칸의 주변 4칸 중 청소 되지 않은 빈 칸의 개수 체크용 변수,
        tmp = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and room[nx][ny] == 0:
                tmp += 1

        # 청소 되지 않은 빈 칸이 하나도 없다면,
        if tmp == 0:
            # 후진
            nx = x + nav[cur_dir - 2][0]
            ny = y + nav[cur_dir - 2][1]
            # 후진한 방의 위치가 벽이라면 종료
            if room[nx][ny] == 1:
                break
            else:
                q.append((nx, ny))
        # 청소 되지 않은 빈 칸이 하나라도 존재 한다면,
        else:
            # 반시계 방향으로 90 회전 후 한칸 전진
            cur_dir = (cur_dir + 1) % 4
            nx = x + nav[cur_dir][0]
            ny = y + nav[cur_dir][1]
            # 이동한 칸이 청소되어 있지 않다면, 해당 칸(nx, ny)을 큐에 추가
            if room[nx][ny] == 0:
                q.append((nx, ny))
            # 이동한 칸이 청소되어 있지 않다면, 이전 칸(x, y)을 큐에 추가
            else:
                q.append((x, y))
    print(cnt)

solution(i, j, d)
