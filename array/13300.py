# 백준 13300 '방 배정'

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

girls = [0] * 6
boys = [0] * 6
rooms = 0

for _ in range(N):
    gender, grade = map(int, input().split())
    if gender == 0:
        girls[grade - 1] += 1
    else:
        boys[grade - 1] += 1

for i in range(6):
    if girls[i] % K == 0:
        rooms += girls[i] // K
    else:
        rooms += (girls[i] // K) + 1

for i in range(6):
    if boys[i] % K == 0:
        rooms += boys[i] // K
    else:
        rooms += (boys[i] // K) + 1

print(rooms)
