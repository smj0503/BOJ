# 백준 1978 '소수 찾기'

import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
ans = 0

def isPrime(n):
    if n == 1:
        return 0

    i = 2
    while i * i <= n:
        if n % i == 0:
            return 0
        i += 1
    return 1

for n in numbers:
    if isPrime(n):
        ans += 1

print(ans)
