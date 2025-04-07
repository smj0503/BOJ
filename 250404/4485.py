# BOJ 4485 '녹색 옷 입은 애가 젤다지?'

import sys
import heapq
input = sys.stdin.readline
INF = 1e9

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dist = [[INF] * n for _ in range(n)]
heap = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

dist[0][0] = graph[0][0]
heapq.heappush(heap, (graph[0][0], 0, 0))

while heap:
    distance,
