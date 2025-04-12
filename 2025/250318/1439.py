# BOJ 1439 '뒤집기'

from collections import deque
import sys
input = sys.stdin.readline

S = deque(list(input().strip()))

short_str = []
x = S.popleft()
short_str.append(x)

while S:
    x = S.popleft()
    if x == short_str[-1]:
        continue
    else:
        short_str.append(x)

zero, one = 0, 0
for s in short_str:
    if s == '0':
        zero += 1
    else:
        one += 1

print(min(zero, one))
