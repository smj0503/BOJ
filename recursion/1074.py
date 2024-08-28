# 백준 1074번 'Z'
# 재귀
# [접근 포인트]
# 1. 함수의 정의
# func(n, r, c)
# 2. base condition
# if n = 0: return 0
# 3. 재귀식
# (r, c)가 1번 사각형 안에 속할 때 -> return func(n-1, r, c)
# (r, c)가 2번 사각형 안에 속할 때 -> return half * half + func(n-1, r, c - half)
# (r, c)가 3번 사각형 안에 속할 때 -> return 2 * half * half + func(n-1, r - half, c)
# (r, c)가 4번 사각형 안에 속할 때 -> return 3 * half * half + func(n-1, r - half, c - half)
# half = 주어진 사각형의 한 변 길이의 절반, 즉 2^(n-1) 이다.

N, r, c = map(int, input().split())

def z(n, r, c):
    if n == 0:
        return 0

    half = 2 ** (n - 1)
    if r < half and c < half:
        return z(n - 1, r, c)
    if r < half <= c:
        return half * half + z(n - 1, r, c - half)
    if c < half <= r:
        return 2 * half * half + z(n - 1, r - half, c)
    return 3 * half * half + z(n - 1, r - half, c - half)

print(z(N, r, c))
