# BOJ 11651

import sys
input = sys.stdin.readline

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

points.sort(key=lambda x : (x[1], x[0]))

for p in points:
    print(*p)
