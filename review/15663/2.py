# BOJ 15663 'N과 M (9)'

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

arr = []
isUsed = [False] * N

def solution(k):
    if k == M:
        print(*arr)

    overlap = 0
    for i in range(N):
        if not isUsed[i] and overlap != numbers[i]:
            arr.append(numbers[i])
            isUsed[i] = True
            overlap = numbers[i]
            solution(k + 1)
            arr.pop()
            isUsed[i] = False

solution(0)
