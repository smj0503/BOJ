# BOJ 1987 '알파벳'

import sys
input = sys.stdin.readline

R, C = map(int, input().split())

board = [list(input().strip()) for _ in range(R)]

ans = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

alph = [False] * 26
alph[ord(board[0][0]) - 65] = True

def solution(x, y, cnt):
    global ans
    ans = max(ans, cnt)

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < R and 0 <= ny < C:
            togo = ord(board[nx][ny]) - 65
            if not alph[togo]:
                alph[togo] = True
                solution(nx, ny, cnt + 1)
                alph[togo] = False

solution(0, 0, 1)
print(ans)

