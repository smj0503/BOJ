# 백준 15649 'N과 M (10)'

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

    overlap = 0  # 중복 탐지용 변수
    for i in range(N):
        if not isUsed[i] and overlap != numbers[i] and (k == 0 or numbers[i] >= arr[-1]):
            arr.append(numbers[i])
            isUsed[i] = True
            overlap = numbers[i]

            backTracking(k + 1)
            arr.pop()
            isUsed[i] = False

backTracking(0)
