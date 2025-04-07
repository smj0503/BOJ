n, m = map(int, input().split())

arr = []
isUsed = [0] * (n+1)

def dfs():
    if len(arr) == m:
        print(*arr)
        return

    for i in range(1, n+1):
        if not isUsed[i]:
            if len(arr) == 0 or arr[-1] < i:
                arr.append(i)
                isUsed[i] = 1
                dfs()
                arr.pop()
                isUsed[i] = 0
    return

dfs()
