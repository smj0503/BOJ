n = 4
arr = []
visited = [0] * n

def dfs():
    if len(arr) == n:
        print(*arr)
        return

    for i in range(n):
        if not visited[i]:
            arr.append(i)
            visited[i] = 1
            dfs()
            arr.pop()
            visited[i] = 0

dfs()
