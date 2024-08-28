# 백준 1697번 '숨바꼭질'
# bfs (1차원)
# [접근 포인트]
# 1. 기존 위치에서 이동하는 위치는 3가지 X - 1, X + 1, X * 2 로 총 3가지가 있다. 즉 노드가 3개로 뻗어 나갈 수 있다.
# 2. 뻗어 나가는 노드가 3개 이므로, 큐에 append할 아이템도 3개이다.
# 3. X - 1, X + 1, X * 2 값이 범위를 넘기지 않도록 한다.

from collections import deque

N, K = map(int, input().split())
MAX = 10 ** 5
dist = [0] * (MAX + 1)

def bfs():
    q = deque()
    q.append(N)

    while q:
        x = q.popleft()

        if x == K:
            return dist[x]

        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)

print(bfs())
