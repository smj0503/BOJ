# 백준 15649 'N과 M (12)'

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

arr = []
isUsed = [0] * N

def func(k):
    if k == M:
        for i in range(M):
            print(arr[i], end=' ')
        print()
        return

    overlap = 0
    for i in range(N):
        if isUsed[i] != M and overlap != numbers[i] and (k == 0 or numbers[i] >= arr[-1]):
            arr.append(numbers[i])
            overlap = numbers[i]
            isUsed[i] += 1

            func(k + 1)
            arr.pop()
            isUsed[i] -= 1

func(0)
