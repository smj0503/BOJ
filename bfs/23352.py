# BOJ 23352 '방탈출'

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(a, b):
    # 시작점으로 부터 각 지점 까지의 거리를 기록용 배열
    dist = [[0 for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((a, b))

    # bfs를 돌려 시작점으로부터 각 지점 까지의 거리를 측정
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] != 0 and dist[nx][ny] == 0:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1

    # 시작점 -> 시작점 거리는 0
    dist[a][b] = 0
    # 도착 지점들 중 거리가 가장 먼 지점의 '좌표'
    fin_x, fin_y = 0, 0
    # 가장 먼 거리
    max_dist = -1

    for i in range(N):
        for j in range(M):
            # 현재 지점 까지의 거리 값이 max_dist 보다 크다면,
            if dist[i][j] > max_dist:
                # max_dist 와 fin_x, fin_y 값 업데이트
                max_dist = dist[i][j]
                fin_x, fin_y = i, j
            # 현재 지점 까지의 거리 값이 max_dist와 같다면
            elif dist[i][j] == max_dist:
                # 두 지점 중 graph의 값이 더 큰 곳의 좌표로 fin_x, fin_y 업데이트
                if graph[i][j] > graph[fin_x][fin_y]:
                    fin_x, fin_y = i, j

    # 다른 지점들과도 'max_dist'와 '시작점 + 끝점' 값을 비교해야 하므로,
    # 둘을 담은 배열을 return
    return [max_dist, graph[a][b] + graph[fin_x][fin_y]]

path = []
# 그래프의 각 점들을 돌며
for i in range(N):
    for j in range(M):
        # 그래프의 값이 0이 아닌 경우, bfs를 실시.
        # 그리고 그 결과 값을 path 배열에 담아준다.
        if graph[i][j] != 0:
            path.append(bfs(i, j))

# path 배열을 내림차순으로 정렬
# 그러면 우선 max_dist 값이 큰 순으로 -> 그 다음엔 '시작점 + 끝점' 값이 큰 순으로 정렬 된다.
path.sort(reverse=True)
# 내림차순 정렬된 path 배열의 제일 첫번째 값[0]의 두번째 요소[1] 출력
print(path[0][1])
