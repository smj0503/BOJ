# 백준 27433번 '팩토리얼 2'
# 재귀
# [접근 포인트]
# 1. 0! = 1, 1! = 1 이므로 n <= 1 일땐 1을 반환. (base condition)
# 2. n! = n * (n-1)!

N = int(input())

def factorial(n):
    if n <= 1:
        ans = 1
    else:
        ans = n * factorial(n-1)

    return ans

print(factorial(N))
