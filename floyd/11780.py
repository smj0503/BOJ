# 백준 11404 '플로이드 2'

import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * n for _ in range(n)]
nxt = [[0] * n for _ in range(n)]

for _ in range(m):
    x, y, c = map(int, input().split())
    graph[x - 1][y - 1] = min(graph[x - 1][y - 1], c)
    nxt[x - 1][y - 1] = y - 1

for i in range(n):
    graph[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                nxt[i][j] = nxt[i][k]

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print("0",  end=" ")
        else:
            print(graph[i][j], end=" ")
    print()

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0 or graph[i][j] == INF:
            print(0)
            continue
        path = []
        st = i
        while st != j:
            path.append(st)
            st = nxt[st][j]
        path.append(j)
        print(len(path), end=' ')
        for p in path:
            print(p + 1, end=' ')
        print()
