# 백준 1644 '소수의 연속합'

import math
import sys
input = sys.stdin.readline

N = int(input())

prime_number = []
temp = [True for _ in range(N + 1)]

for i in range(2, int(math.sqrt(N)) + 1):
    if temp[i]:
        j = 2

        # i의 배수는 모두 false 처리. 즉 소수가 아닌 수는 모두 false 처리 될 것이다.
        while i * j <= N:
            temp[i * j] = False
            j += 1

for num in range(2, N + 1):
    if temp[num]:
        prime_number.append(num)

count = 0
interval_sum = 0
en = 0

for st in range(len(prime_number)):
    while interval_sum < N and en < len(prime_number):
        interval_sum += prime_number[en]
        en += 1

    if interval_sum == N:
        count += 1
    interval_sum -= prime_number[st]

print(count)
