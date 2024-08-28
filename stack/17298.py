# BOJ 17298 '오큰수'

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

nge = [-1] * N
stack = deque()

for i in range(N):
    while stack and nums[stack[-1]] < nums[i]:
        idx = stack.pop()
        nge[idx] = nums[i]
    stack.append(i)

print(*nge)
