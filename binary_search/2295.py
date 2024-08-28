# 백준 2295 '세 수의 합'
# 접근 포인트
# x + y + z = k 라면, x + y = k - z 도 성립 한다.

import sys
input = sys.stdin.readline

N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()

sum_of_two = set()
for a in numbers:
    for b in numbers:
        sum_of_two.add(a + b)

ans = []
for a in numbers:
    for b in numbers:
        if a - b in sum_of_two:
            ans.append(a)

ans.sort()
print(ans[-1])
