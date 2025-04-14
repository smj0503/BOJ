# BOJ 1753 '최단경로'

import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

v, e = map(int, input().split())
k = int(input())
INF = int(1e9)

# 그래프 초기화
graph = [[] * (v+1) for _ in range(v+1)]
distance = [INF] * (v+1)

# 간선 정보 입력
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드의 인접 노드 확인
        for node in graph[now]:
            v, w = node
            cost = dist + w
            # 현재 노드를 거쳐 가는 거리가 더 짧은 경우 => 갱신
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))

dijkstra(k)

for i in range(1, v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
