# 백준 10816번 '숫자 카드 2'

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

def lower_index(target):
    st = 0
    en = N

    while st < en:
        mid = (st + en) // 2
        if arr[mid] >= target:
            en = mid
        else:
            st = mid + 1

    return st

def upper_index(target):
    st = 0
    en = N

    while st < en:
        mid = (st + en) // 2
        if arr[mid] > target:
            en = mid
        else:
            st = mid + 1

    return st

arr.sort()
for t in targets:
    print(upper_index(t) - lower_index(t))
