# 백준 9095번 '1, 2, 3 더하기'

import sys
input = sys.stdin.readline

T = int(input())
tc = [int(input()) for _ in range(T)]

d = [0] * 11
d[1] = 1
d[2] = 2
d[3] = 4

for i in range(4, 11):
    d[i] = d[i-1] + d[i-2] + d[i-3]

for t in tc:
    print(d[t])
