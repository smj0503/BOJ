# 백준 1629번 '곱셈'
# 재귀
# [접근 포인트]
# 1. A^(m+n) = A^m x A^n                  -> 지수 법칙
# 2. (A x B) % C = (A % C) * (B % C) % C   -> 나머지 분배 법칙

A, B, C = map(int, input().split())

def pow(a, b, c):
    if b == 1:
        return a % c

    val = pow(a, b // 2, c)
    val = val * val % c

    if b % 2 == 0:
        return val

    return val * a % c

print(pow(A, B, C))
