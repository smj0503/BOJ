# 백준 14938 '서강그라운드'

import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(r):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
    graph[b][a] = min(graph[b][a], c)

for i in range(1, n + 1):
    graph[i][i] = 0

# 플로이드 알고리즘
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = 0

for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if graph[i][j] <= m:
            count += items[j]
    result = max(result, count)

print(result)
