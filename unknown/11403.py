# BOJ 11403 '경로 찾기'

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# BFS
isConnected = [[0] * N for _ in range(N)]

def bfs(start):
    q = deque([start])
    visited = [0 for _ in range(N)]

    while q:
        x = q.popleft()

        for i in range(N):
            if visited[i] == 0 and graph[x][i] == 1:
                q.append(i)
                visited[i] = 1
                isConnected[start][i] = 1

for i in range(N):
    bfs(i)
for c in isConnected:
    print(*c)

# 플로이드 알고리즘
# for k in range(N):
#     for i in range(N):
#         for j in range(N):
#             if graph[i][k] == 1 and graph[k][j] == 1:
#                 graph[i][j] = 1
#
# for g in graph:
#     print(*g)
