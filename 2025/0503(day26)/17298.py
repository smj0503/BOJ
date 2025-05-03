# BOJ 17298

import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

nge = [-1] * n
stack = []

for i in range(n):
    while stack and a[stack[-1]] < a[i]:
        idx = stack.pop()
        nge[idx] = a[i]
    stack.append(i)

print(*nge)
