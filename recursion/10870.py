# 백준 10870번 '피보나치 수 5'
# 재귀
# [접근 포인트]
# 1. n이 0일때는 0, n이 1일때는 1이므로 n<=1 일때는 n을 반환
# 2. 피보나치 수는 앞의 두 피보나치 수의 합이므로,
#    n번째 피보나치 수는 (n-1)번째 피보나치 수와 (n-2)번째 피보나치 수의 합이다.

N = int(input())

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(N))
