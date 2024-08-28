# 백준 1759 '암호 만들기'

import sys
input = sys.stdin.readline

L, C = map(int, input().split())
alps = list(input().split())
alps.sort()

isUsed = [False] * C
crypto = []

def func(cur):
    if cur == L:
        vows = 0
        cons = 0
        for c in crypto:
            if c in 'aeiou':
                vows += 1
            else:
                cons += 1

        if vows > 0 and cons > 1:
            for c in crypto:
                print(c, end='')
            print()
        return

    for i in range(C):
        if not isUsed[i] and (cur == 0 or alps[i] > crypto[-1]):
            isUsed[i] = True
            crypto.append(alps[i])

            func(cur + 1)
            isUsed[i] = False
            crypto.pop()

func(0)
