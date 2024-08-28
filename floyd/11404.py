# 백준 11404 '플로이드'

import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * n for _ in range(n)]

for _ in range(m):
    x, y, c = map(int, input().split())
    graph[x - 1][y - 1] = min(graph[x - 1][y - 1], c)

for i in range(n):
    graph[i][i] = 0

# 중요!) 테이블을 갱신할 때 중간에 거쳐 가게끔 할 원소(k)를 3중 for문의 제일 바깥에 두어야 함.
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print("0",  end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
