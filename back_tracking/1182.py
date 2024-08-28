# 백준 1182 '부분 수열의 합'

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = 0

def func(cur, sum):
    global cnt

    if cur == N:
        if sum == S: cnt += 1
        return

    func(cur + 1, sum)
    func(cur + 1, sum + numbers[cur])

func(0, 0)

if S == 0: cnt -= 1
print(cnt)
