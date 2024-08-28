# 백준 1260번 'DFS와 BFS'

from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for vertex in graph:
    vertex.sort()

def DFS(start):
    visited[start] = 1
    print(start, end=" ")

    for node in graph[start]:
        if not visited[node]:
            DFS(node)

def BFS(start):
    q = deque([start])
    visited[start] = 1

    while q:
        cur = q.popleft()
        print(cur, end=" ")

        for node in graph[cur]:
            if not visited[node]:
                visited[node] = 1
                q.append(node)

visited = [0] * (N + 1)
DFS(V)
print()
visited = [0] * (N + 1)
BFS(V)
