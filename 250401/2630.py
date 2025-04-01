# BOJ 2630 '색종이 만들기'

import sys
input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

white = 0
blue = 0

def check(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != paper[x][y]:
                return False
    return True

def dfs(x, y, n):
    global white, blue
    if check(x, y, n):
        if paper[x][y] == 0:
            white += 1
        else:
            blue += 1
        return

    n //= 2
    for i in range(2):
        for j in range(2):
            dfs(x + i * n, y + j * n, n)

dfs(0, 0, N)
print(white)
print(blue)
