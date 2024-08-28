# 백준 2606번 '바이러스'
# bfs

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
link = int(input())

network = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for i in range(link):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

cnt = 0

def BFS(virus):
    global cnt
    queue = deque()
    queue.append(virus)

    while queue:
        cur = queue.popleft()
        visited[cur] = 1
        for i in network[cur]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)
                cnt += 1

BFS(1)
print(cnt)
