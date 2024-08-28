# 백준 11328 'Strfry'

import sys
input = sys.stdin.readline

N = int(input())
cases = []
for _ in range(N):
    word1, word2 = map(str, input().split())
    cases.append([word1, word2])

for c in cases:
    if sorted(list(c[0])) == sorted(list(c[1])):
        print('Possible')
    else:
        print('Impossible')
