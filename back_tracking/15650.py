# 백준 15650 'N과 M (2)'
# 중복 허용 X, 오름차순

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] * M
isUsed = [False] * (N + 1)

def backTracking(k):
    if k == M:
        for i in range(M):
            print(arr[i], end=' ')
        print()
        return

    for i in range(1, N + 1):
        if not isUsed[i] and (k == 0 or i > arr[k - 1]):
            arr[k] = i
            isUsed[i] = True
            backTracking(k + 1)
            # 재귀 끝난 뒤 빠져 나와서 바로 직전에 담았던 것 제거
            isUsed[i] = False

backTracking(0)
