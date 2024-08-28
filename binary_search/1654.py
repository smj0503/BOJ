# 백준 1654 '랜선 자르기'
# 접근 포인트
# 최소 길이를 1로 설정하고, 최대 길이를 가지고 있는 랜선 중 가장 긴 길이로 설정한다.
# 그 후 이분 탐색을 실시

# Parametric Search
# 최적화 문제 : N개를 만들 수 있는 랜선의 최대 길이
# 결정 문제 : 랜선의 길이가 X일 때 랜선이 N개 이상인가 아닌가?

import sys
input = sys.stdin.readline

K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]
cables.sort()

st = 1
en = max(cables)

while st <= en:
    mid = (st + en) // 2
    lines = 0

    for c in cables:
        lines += c // mid

    if lines >= N:
        st = mid + 1
    else:
        en = mid - 1

print(en)
