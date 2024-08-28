# 백준 2512 '예산'

import sys
input = sys.stdin.readline

N = int(input())
local = list(map(int, input().split()))
national = int(input())

local.sort()
st = 1
en = local[-1]

while st <= en:
    mid = (st + en) // 2
    total = 0

    for l in local:
        if l <= mid:
            total += l
        else:
            total += mid

    if total <= national:
        st = mid + 1
    else:
        en = mid - 1

print(en)
