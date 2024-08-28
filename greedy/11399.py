# 백준 11399 'ATM'

import sys
input = sys.stdin.readline

N = int(input())
people = sorted(list(map(int, input().split())))
ans = 0
cur = 0

for p in people:
    cur += p
    ans += cur

print(ans)
