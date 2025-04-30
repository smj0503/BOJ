# PROGRAMMERS 121690 '보물지도'

from collections import deque

def solution(n, m, hole):
    INF = int(1e9)

    grid = [[0] * m for _ in range(n)]
    for a, b in hole:
        grid[a-1][b-1] = 1

    # visited[i][j][0] : grid[i][j]를 아이템 안쓰고 방문
    # visited[i][j][1] : grid[i][j]를 아이템 쓰고 방문
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    distance = [[[INF] * 2 for _ in range(m)] for _ in range(n)]

    q = deque()
    q.append((0, 0, 0))     # (i,j,아이템 사용 유무)
    visited[0][0][0] = 1    # 아이템 안쓰고 (0,0) 방문
    distance[0][0][0] = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while q:
        x, y, item = q.popleft()
        # 아이템 아직 사용 안함 -> (한칸 이동), (두칸 이동) 모두 가능
        if item == 0:
            # 두칸 이동(아이템 사용)
            for i in range(4):
                nx, ny = x + 2 * dx[i], y + 2*dy[i]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][1] == 0 and grid[nx][ny] == 0:
                    # 방문 처리
                    visited[nx][ny][1] = 1
                    # [1]
                    distance[nx][ny][1] = min(distance[nx][ny][1], distance[x][y][0] + 1)
                    q.append((nx, ny, 1))
            # 한칸 이동
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][item] == 0 and grid[nx][ny] == 0:
                    # 방문 처리
                    visited[nx][ny][0] = 1
                    # [0]
                    distance[nx][ny][0] = min(distance[nx][ny][0], distance[x][y][0] + 1)
                    q.append((nx, ny, item))
        # 아이템 이미 사용 -> (한칸 이동)만 가능
        else:
            # distance[new_x][new_y][1] 에 저장
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][1] == 0 and grid[nx][ny] == 0:
                    # 방문 처리
                    visited[nx][ny][1] = 1
                    distance[nx][ny][1] = min(distance[nx][ny][1], distance[x][y][1] + 1)
                    q.append((nx, ny, 1))

    if distance[n-1][m-1][1] != INF:
        return distance[n-1][m-1][1]
    else:
        return -1
