# 백준 10815 '숫자 카드'

import sys
input = sys.stdin.readline

N = int(input())
cards = list(map(int, input().split()))
M = int(input())
numbers = list(map(int, input().split()))

cards.sort()

def binary_search(target):
    st = 0
    en = N - 1

    while st <= en:
        mid = (en + st) // 2
        if cards[mid] < target:
            st = mid + 1
        elif cards[mid] > target:
            en = mid - 1
        else:
            return 1

    return 0

for n in numbers:
    print(binary_search(n), end=' ')
