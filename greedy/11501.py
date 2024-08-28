# 백준 11501 '주식'

import sys
input = sys.stdin.readline

T = int(input())
results = []

for _ in range(T):
    N = int(input())
    chart = list(map(int, input().split()))
    chart.reverse()

    max_value = chart[0]
    profit = 0

    for i in range(1, N):
        if max_value < chart[i]:
            max_value = chart[i]
            continue
        profit += max_value - chart[i]

    results.append(profit)

for r in results:
    print(r)
