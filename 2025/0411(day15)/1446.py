# BOJ 1446

# 다익스트라 풀이
import heapq

def dijkstra(start):
    q = []
    # 시작 노드를 우선순위 큐에 넣음 (거리, 노드번호)
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, cur = heapq.heappop(q)

        # 이미 더 짧은 경로로 방문한 적 있으면 스킵
        if distance[cur] < dist:
            continue

        # 현재 노드에서 갈 수 있는 모든 노드를 확인
        # graph[cur] : (도착노드, 거리) 형태의 튜플 리스트
        for node in graph[cur]:
            cost = dist + node[1]

            if distance[node[0]] > cost:
                distance[node[0]] = cost
                heapq.heappush(q, (cost, node[0]))

n, d = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(d+1)]
distance = [INF] * (d+1)

# 기본적으로, i -> i+1 도로는 항상 존재하고 거리는 1이다 (초기화)
# 즉, 지름길이 없더라도 0 → 1 → 2 → ... → d 로 도달할 수 있게 보장
for i in range(d):
    graph[i].append((i+1, 1))

for _ in range(n):
    st, en , length = map(int, input().split())
    # 지름길의 도착지점이 d보다 크면 의미가 없으므로 무시
    if en > d:
        continue
    graph[st].append((en, length))

dijkstra(0)
print(distance[d])
