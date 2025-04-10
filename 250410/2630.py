# BOJ 2630

import sys
input = sys.stdin.readline

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
colors = [0, 0]

def check_area(x, y, z):
    for i in range(x, x + z):
        for j in range(y, y + z):
            if paper[x][y] != paper[i][j]:
                return False
    return True

def func(x, y, z):
    if check_area(x, y, z):
        colors[paper[x][y]] += 1
        return

    z //= 2
    for i in range(2):
        for j in range(2):
            func(x + i*z, y + j*z, z)

func(0, 0, n)
for c in colors:
    print(c)
