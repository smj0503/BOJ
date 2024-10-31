# BOJ 2096 '내려가기'

import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
dp_max = numbers
dp_min = numbers

for _ in range(N - 1):
    x, y, z = map(int, input().split())
    dp_max = [x + max(dp_max[0], dp_max[1]), y + max(dp_max), z + max(dp_max[1], dp_max[2])]
    dp_min = [x + min(dp_min[0], dp_min[1]), y + min(dp_min), z + min(dp_min[1], dp_min[2])]

print(max(dp_max), min(dp_min))
