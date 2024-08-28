# 백준 1929 '소수 구하기'

import math

M, N = map(int, input().split())

def sieve(m, n):
    state = [True] * (n + 1)
    state[1] = False

    for i in range(2, int(math.sqrt(n)) + 1):
        if not state[i]: continue
        for j in range(i * i, n + 1, i):
            state[j] = False

    for i in range(m, n + 1):
        if state[i]:
            print(i)

sieve(M, N)
