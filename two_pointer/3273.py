# 백준 3273 '두 수의 합'

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()
cnt = 0
st = 0
en = N - 1

while st < en:
    temp = arr[st] + arr[en]
    if temp == x:
        cnt += 1
        st += 1
    elif temp < x:
        st += 1
    else:
        en -= 1

print(cnt)
