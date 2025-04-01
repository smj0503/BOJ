# BOJ 4307 '개미'

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    stick, n = map(int, input().split())
    ants = [int(input()) for _ in range(n)]

    short = []
    long = []

    for ant in ants:
        short.append(min(ant, stick - ant))
        long.append(max(ant, stick - ant))

    print(max(short), max(long))
