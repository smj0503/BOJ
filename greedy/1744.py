# 백준 1744 '수 묶기"

import sys
input = sys.stdin.readline

N = int(input())
# 양수 배열
positives = []
# 음수 배열
negatives = []
# 최대 합
max_sum = 0

for _ in range(N):
    num = int(input())
    if num > 0:
        positives.append(num)
    else:
        negatives.append(num)

positives.sort(reverse=True)
negatives.sort()

while positives:
    if len(positives) > 1:
        a = positives.pop(0)
        b = positives.pop(0)
        if a == 1 or b == 1:
            max_sum += (a + b)
        else:
            max_sum += a * b
    else:
        max_sum += positives.pop(0)

while negatives:
    if len(negatives) > 1:
        a = negatives.pop(0)
        b = negatives.pop(0)
        max_sum += a * b
    else:
        max_sum += negatives.pop(0)

print(max_sum)
