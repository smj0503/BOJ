# 백준 2470 '두 용액'

import sys
input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

st = 0
en = N - 1

mix = abs(liquid[st] + liquid[en])
ans = [liquid[st], liquid[en]]

while st < en:
    temp = liquid[st] + liquid[en]

    if abs(temp) < mix:
        mix = abs(temp)
        ans = [liquid[st], liquid[en]]
        if mix == 0:
            break
    if temp < 0:
        st += 1
    else:
        en -= 1

print(ans[0], ans[1])
