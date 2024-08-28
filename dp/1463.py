# 백준 1463번 '1로 만들기'

import sys
input = sys.stdin.readline

N = int(input())
dist = [0, 0]

for i in range(2, N + 1):
    # 1을 빼는 경우
    dist.append(dist[i - 1] + 1)
    # 2로 나누는 경우
    if i % 2 == 0:
        dist[i] = min(dist[i], dist[i // 2] + 1)
    # 3으로 나누는 경우
    if i % 3 == 0:
        dist[i] = min(dist[i], dist[i // 3] + 1)

print(dist[-1])
