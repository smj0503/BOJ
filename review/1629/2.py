# BOJ 1629 '곱셈'

A, B, C = map(int, input().split())

def solution(a, b, c):
    if b == 1:
        return a % c

    temp = solution(a, b // 2, c)
    temp = temp * temp % c

    if b % 2 == 0:
        return temp

    return temp * a % c

print(solution(A, B, C))
