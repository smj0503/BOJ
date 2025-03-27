# BOJ 15649

N, M = map(int, input().split())
ans = []
visited = [0] * (N + 1)

def dfs():
    if len(ans) == M:
        print(*ans)
        return

    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = 1
            ans.append(i)
            dfs()
            visited[i] = 0
            ans.pop()

dfs()
