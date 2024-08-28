# 백준 2805 '나무 자르기'

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()

st = 1
en = max(tree)

while st <= en:
    mid = (st + en) // 2
    cutting = 0

    for t in tree:
        if t - mid > 0:
            cutting += (t - mid)

    # 톱날의 높이 더 높여야 됨
    if cutting >= M:
        st = mid + 1
    # 톱날의 높이 낮춰야 됨
    else:
        en = mid - 1

print(en)
