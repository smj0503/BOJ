# 백준 2847 '게임을 만든 동준이'

import sys
input = sys.stdin.readline

# 레벨의 수
N = int(input())
scores = [int(input()) for _ in range(N)]
scores.reverse()

max_score = scores[0]
ans = 0

for i in range(1, N):
    if scores[i] >= max_score:
        ans += (scores[i] - max_score) + 1
        max_score -= 1
    else:
        max_score = scores[i]

print(ans)
