# 백준 11047 '동전 0'

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)

count = 0
goal = K

for coin in coins:
    if goal == 0:
        break

    if coin <= goal:
        count += (goal // coin)
        goal = goal % coin

print(count)
