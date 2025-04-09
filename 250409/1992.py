# BOJ 1992

import sys
input = sys.stdin.readline

n = int(input())
quad = [list(input().strip()) for _ in range(n)]
ans = ''

def check_area(x, y, z):
    for i in range(x, x + z):
        for j in range(y, y + z):
            if quad[i][j] != quad[x][y]:
                return False
    return True

def func(x, y, z):
    global ans
    if check_area(x, y, z):
        ans += quad[x][y]
        return

    ans += '('
    z //= 2
    for i in range(2):
        for j in range(2):
            func(x + i*z, y + j*z, z)
    ans += ')'
    return

func(0, 0, n)
print(ans)
