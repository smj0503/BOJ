# BOJ 4307

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    l, n = map(int, input().split())
    ants = [int(input()) for _ in range(n)]

    shortest = 0
    longest = 0

    for ant in ants:
        short = min(ant, l-ant)
        long = max(ant, l-ant)

        shortest = max(shortest, short)
        longest = max(longest, long)

    print(shortest, longest)
