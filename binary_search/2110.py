# 백준 2110 '공유기 설치'

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
house = [int(input()) for _ in range(N)]
house.sort()

st = 1
en = house[-1] - house[0]   # 최대 공유기 거리는 "맨 끝 집 - 맨 첫 집"
ans = 0

while st <= en:
    mid = (st + en) // 2
    current = house[0]  # 첫번째 집 부터 탐색 시작
    count = 1           # 항상 1번째 집에 공유기를 설치

    for i in range(1, N):
        if house[i] >= current + mid:
            count += 1
            current = house[i]

    if count >= C:
        st = mid + 1
        ans = mid
    else:
        en = mid - 1

print(ans)
