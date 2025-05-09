# BOJ 11724

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def bfs(start):
    q = deque()
    q.append(start)

    while q:
        x = q.popleft()
        for node in graph[x]:
            if not visited[node]:
                visited[node] = 1
                q.append(node)

cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        bfs(i)
        cnt += 1

print(cnt)
