# BOJ 1629 '곱셈'
# 지수 법칙 : A^(m+n) = A^m x A^n
# 나머지 분배 법칙 : (A x B) % C = (A % C) * (B % C) % C

import sys
sys.setrecursionlimit(10**8)

A, B, C = map(int, input().split())

def solution(a, b, c):
    if b == 1:
        return a % c

    val = solution(a, b // 2, c)
    val = val * val % c

    if b % 2 == 0:
        return val

    return val * a % c

print(solution(A, B, C))
