# BOJ 15663 'N과 M (9)'

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

isUsed = [False] * N
arr = []

def solution(k):
    if k == M:
        print(*arr)

    overlap = 0
    for i in range(N):
        if not isUsed[i] and numbers[i] != overlap:
            isUsed[i] = True
            arr.append(numbers[i])
            overlap = numbers[i]

            solution(k + 1)
            isUsed[i] = False
            arr.pop()

solution(0)
