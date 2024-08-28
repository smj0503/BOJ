# 백준 15649 'N과 M (7)'
# 중복 허용

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

arr = []
isUsed = [0] * N

def backTracking(k):
    if k == M:
        for i in range(M):
            print(arr[i], end=' ')
        print()
        return

    for i in range(N):
        if isUsed[i] != M:
            arr.append(numbers[i])
            isUsed[i] += 1
            backTracking(k + 1)
            arr.pop()
            isUsed[i] -= 1

backTracking(0)
