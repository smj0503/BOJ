# BOJ 1439 '뒤집기'

import sys
input = sys.stdin.readline
S = input()

cnt_zero = 0
cnt_one = 0

for i in range(len(S) - 1):
    if S[i] != S[i + 1]:
        if S[i] == '0':
            cnt_zero += 1
        else:
            cnt_one += 1

print(min(cnt_zero, cnt_one))
