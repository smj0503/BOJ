# 백준 1992 '쿼드트리'

import sys
input = sys.stdin.readline

N = int(input())
display = []
for _ in range(N):
    display.append(list(input().strip()))
result = ''

def check(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if display[x][y] != display[i][j]:
                return False
    return True

def func(x, y, z):
    global result
    if check(x, y, z):
        result += display[x][y]
        return

    result += '('
    n = z // 2
    for i in range(2):
        for j in range(2):
            func(x + i * n, y + j * n, n)
    result += ')'

func(0, 0, N)
print(result)
