# BOJ 11659 '구간 합 구하기 4'

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# 누적 합 배열
sum_arr = []
temp = 0
for i in range(N+1):
    temp += arr[i]
    sum_arr.append(temp)

for _ in range(M):
    i, j = map(int, input().split())
    # i부터 j까지의 구간합을 구하기 위해선,
    # j의 누적합에서 i-1의 누적합을 빼줍니다.
    print(sum_arr[j] - sum_arr[i-1])
