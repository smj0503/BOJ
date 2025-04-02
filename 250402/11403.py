# BOJ 11403

import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for x in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][x] == 1 and graph[x][j] == 1:
                graph[i][j] = 1

for line in graph:
    print(*line)
