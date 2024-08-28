# 백준 10807 '개수 세기'

import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
v = int(input())

ans = 0
for n in numbers:
    if n == v:
        ans += 1

print(ans)
