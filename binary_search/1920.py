# 백준 1920번 '수 찾기'

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

def binary_search(target):
    st = 0
    en = N - 1

    while st <= en:
        mid = (st + en) // 2
        if arr[mid] < target:
            st = mid + 1
        elif arr[mid] > target:
            en = mid - 1
        else:
            return 1

    return 0

arr.sort()
for t in targets:
    print(binary_search(t))
