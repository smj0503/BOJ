# 백준 2775 '부녀회장이 될테야'

import sys
input = sys.stdin.readline

T = int(input())
cases = []

for _ in range(T):
    k = int(input())
    n = int(input())
    cases.append([k, n])

print(cases)
