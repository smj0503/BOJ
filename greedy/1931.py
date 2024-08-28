# 백준 1931 '회의실 배정'

import sys
input = sys.stdin.readline

N = int(input())
meeting = []
for _ in range(N):
    start, end = map(int, input().split())
    meeting.append([end, start])
meeting.sort()

t = 0   # 현재 시간
ans = 0 # 답

for i in range(N):
    # 지금 보는 스케줄의 시작 시간이 t 이하면 바로 회의를 배정한다.
    if t > meeting[i][1]:
        continue
    ans += 1            # 회의 배정
    t = meeting[i][0]   # 현재 시간 t는 배정된 회의의 끝나는 시간으로 변경.

print(ans)

