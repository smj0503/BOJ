# 백준 2630 '색종이 만들기'

import sys
input = sys.stdin.readline

N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

# 앞에서 부터 흰종이, 파란 종이
cnt = [0, 0]

def check(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[x][y] != paper[i][j]:
                return False
    return True

def func(x, y, z):
    if check(x, y, z):
        cnt[paper[x][y]] += 1
        return

    n = z // 2
    for i in range(2):
        for j in range(2):
            func(x + i * n, y + j * n, n)

func(0, 0, N)
for c in cnt:
    print(c)
