# BOJ 1992

import sys
input = sys.stdin.readline

N = int(input())
graph = [list(input().strip()) for _ in range(N)]

answer = ''

def check(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if graph[i][j] != graph[x][y]:
                return False
    return True

def dfs(x, y, n):
    global answer
    if check(x, y, n):
        answer += graph[x][y]
        return

    answer += '('
    n = n // 2
    for i in range(2):
        for j in range(2):
            dfs(x + i * n, y + j * n, n)
    answer += ')'

dfs(0, 0, N)
print(answer)
