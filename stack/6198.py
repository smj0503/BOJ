# BOJ 6198 '옥상 정원 꾸미기'

import sys
input = sys.stdin.readline

N = int(input())
buildings = []
for _ in range(N):
    buildings.append(int(input()))

cnt = 0
stack = []

for b in buildings:
    # stack이 비어 있지 않고,
    # stack의 top 보다 큰 값이 들어온다면
    while stack and b >= stack[-1]:
        # stack pop
        stack.pop()
    stack.append(b)
    # (스택의 크기 - 1) 만큼 카운트
    cnt += (len(stack) - 1)

print(cnt)
