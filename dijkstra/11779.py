# 백준 11779 '최소비용 구하기 2'

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

dist = [INF] * (n + 1)
# pre : 경로 복원용 배열
pre = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))
st, en = map(int, input().split())

dist[st] = 0
pq = [(0, st)]

while pq:
    cur_cost, cur = heapq.heappop(pq)

    if dist[cur] != cur_cost:
        continue

    for nxt_cost, nxt in graph[cur]:
        if dist[nxt] > cur_cost + nxt_cost:
            dist[nxt] = cur_cost + nxt_cost
            heapq.heappush(pq, (dist[nxt], nxt))
            pre[nxt] = cur

# path : 경로 출력 용 배열
path = []
print(dist[en])

cur = en
while cur != st:
    path.append(cur)
    cur = pre[cur]
path.append(cur)
path.reverse()

print(len(path))
for p in path:
    print(p, end=' ')
