# 백준 25501번 '재귀의 귀재'
# 재귀
# [중요 포인트]
# 재귀 함수의 호출 횟수를 담는 변수 cnt를 전역 변수(글로벌 변수)로 선언해준다.

import sys
input = sys.stdin.readline

T = int(input())

def recursion(s, l, r):
    global cnt # 함수 내에서 전역 변수로 cnt를 활용하기 위해 global로 명시해준다.
    cnt += 1

    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else:
        return recursion(s, l+1, r-1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

for _ in range(T):
    cnt = 0
    print(isPalindrome(input()), cnt)
