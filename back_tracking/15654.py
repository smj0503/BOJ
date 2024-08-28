# 백준 15649 'N과 M (5)'
# 중복 허용 X

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

arr = []
isUsed = [False] * N

def backTracking(k):
    if k == M:
        for i in range(M):
            print(arr[i], end=' ')
        print()
        return

    for i in range(N):
        if not isUsed[i]:
            arr.append(numbers[i])
            isUsed[i] = True
            backTracking(k + 1)
            arr.pop()
            isUsed[i] = False

backTracking(0)
