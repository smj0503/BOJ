# 백준 1822 '차집합'

import sys
input = sys.stdin.readline

num_A, num_B = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

def binary_search(target):
    st = 0
    en = num_B - 1

    while st <= en:
        mid = (st + en) // 2
        if B[mid] < target:
            st = mid + 1
        elif B[mid] > target:
            en = mid - 1
        else:
            return 1

    return 0

ans = []
for num in A:
    if not binary_search(num):
        ans.append(num)

if len(ans) == 0:
    print(0)
else:
    print(len(ans))
    print(*ans)
