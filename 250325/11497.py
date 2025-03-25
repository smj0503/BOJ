# BOJ 11497 '통나무 건너뛰기'

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    timbers = list(map(int, input().split()))
    timbers.sort()

    ans = 0
    front = []
    rear = []
    for i in range(N):
        if i % 2 == 0:
            front.append(timbers[i])
        else:
            rear.append(timbers[i])
    rear.reverse()

    new_arr = front + rear
    for i in range(1, N):
        ans = max(ans, abs(new_arr[i] - new_arr[i-1]))

    print(ans)
