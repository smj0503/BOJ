# BOJ 3980 '선발 명단'

import sys
input = sys.stdin.readline

C = int(input())

# count : 포지션(j) 기준
def solution(count, total):
    global answer
    if count == 11:
        answer = max(answer, total)
        return

    for i in range(11):
        if not selected[i] and players[count][i] != 0:
            selected[i] = True
            solution(count + 1, total + players[count][i])
            selected[i] = False

for _ in range(C):
    players = [list(map(int, input().split())) for _ in range(11)]
    selected = [False] * 11
    answer = 0

    solution(0, 0)
    print(answer)
