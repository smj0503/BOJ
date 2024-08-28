# 백준 15649 'N과 M (11)'

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

    overlap = 0  # 중복 탐지용 변수
    for i in range(N):
        if isUsed[i] != M and overlap != numbers[i]:
            arr.append(numbers[i])
            isUsed[i] += 1
            overlap = numbers[i]

            backTracking(k + 1)
            arr.pop()
            isUsed[i] -= 1

backTracking(0)
