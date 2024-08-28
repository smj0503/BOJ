# 백준 2170 '선 긋기'

import sys
input = sys.stdin.readline

N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]
lines.sort()

ans = 0
st, en = lines[0]

for i in range(1, N):
    x, y = lines[i]

    # 겹치는 경우
    if x <= en:
        en = max(en, y)
    # 겹치지 않는 경우
    else:
        ans += (en - st)
        st, en = x, y

ans += (en - st)
print(ans)
