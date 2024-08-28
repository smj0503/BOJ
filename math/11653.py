# # 백준 11653 '소인수분해'

import math

N = int(input())

def factorization(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            print(i)
            n //= i

    if n != 1:
        print(n)

factorization(N)
