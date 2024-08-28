# 백준 1439 '뒤집기'

import sys
input = sys.stdin.readline
s = input()

count_zero = 0
count_one = 0

for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        if s[i] == '0':
            count_zero += 1
        else:
            count_one += 1

print(min(count_zero, count_one))
