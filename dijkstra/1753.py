# 백준 1753 '최단 경로'

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
K = int(input())

dist = [INF] * (V + 1) # 최단 거리 테이블
graph = [[] for _ in range(V + 1)]

# 그래프 채우기
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

# 시작점(K)의 거리는 0으로 설정
dist[K] = 0
# 우선 순위 큐 pq 생성 하고, (0, K) 삽입 (0: 시작점의 가중치, K: 시작점 번호)
pq = [(0, K)]

# 다익스트라 알고리즘 시작
while pq:
    # 우선 순위 큐에서 가중치가 가장 작은 원소(cur_cost, cur)를 선택, 해당 가중치가 최단 거리 테이블에 있는 값과 다를 경우 넘어감
    cur_cost, cur = heapq.heappop(pq)

    if dist[cur] != cur_cost:
        continue

    # cur와 이웃한 정점들에 대해
    for nxt_cost, nxt in graph[cur]:
        # 최단 거리 테이블 값보다 cur를 거쳐 가는 것이 더 작은 값을 가질 경우
        if dist[nxt] > cur_cost + nxt_cost:
            # 최단 거리 테이블의 값을 갱신 하고 우선 순위 큐에 (가중치, 이웃한 정점의 번호)를 추가
            dist[nxt] = cur_cost + nxt_cost
            heapq.heappush(pq, (dist[nxt], nxt))

# 출력
for i in range(1, V + 1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
