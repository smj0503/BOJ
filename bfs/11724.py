# 백준 11724번 '연결 요소의 개수'

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def BFS(start):
    q = deque()
    q.append(start)

    while q:
        cur = q.popleft()
        visited[cur] = 1

        for node in graph[cur]:
            if not visited[node]:
                visited[node] = 1
                q.append(node)

cnt = 0

for i in range(1, N + 1):
    if not visited[i]:
        BFS(i)
        cnt += 1

print(cnt)
