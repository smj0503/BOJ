# 백준 9663 'N-QUEEN'
# [접근 포인트]
# 0. 한 행에는 하나의 Queen만 놓일 수 있으므로 같은 행일 경우는 고려x
# 1. 같은 열에 위치 하는지를 확인 하려면? -> y좌표가 일치 하는지를 확인
# 2. 같은 /(우상향) 대각선 위에 위치 하는지를 확인 하려면? -> x + y 값이 일치 하는지를 확인
# 3. 같은 \(우하향) 대각선 위에 위치 하는지를 확인 하려면? -> x - y 값이 일치 하는지를 확인

# 1, 2, 3 각각에 대응되는 isUsed1, isUsed2, isUsed3 배열을 생성.
# isUsed1 : 열에 대응되는 배열. (x, y)에 퀸이 있으면 isUsed1[y] = True (배열 크기 : n)
# isUsed2 : 우상향 대각선(/)에 대응되는 배열. (x, y)에 퀸이 있으면 isUsed2[x+y] = True (배열 크기 : 2n - 1)
# isUsed3 : 우하향 대각선(\)에 대응되는 배열. (x, y)에 퀸이 있으면 isUsed3[(x-y)+(n-1)] = True (배열 크기 : 2n - 1)

import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

isUsed1 = [0] * N
isUsed2 = [0] * (2*N - 1)
isUsed3 = [0] * (2*N - 1)

def n_queen(cur):
    global cnt
    if cur == N:
        cnt += 1
        return

    for i in range(N):
        if isUsed1[i] or isUsed2[cur+i] or isUsed3[cur-i+N-1]:
            continue
        # is used 표시
        isUsed1[i] = True
        isUsed2[cur+i] = True
        isUsed3[cur-i+N-1] = True
        # 재귀 호출
        n_queen(cur+1)
        # is used 표시 해제
        isUsed1[i] = False
        isUsed2[cur+i] = False
        isUsed3[cur-i+N-1] = False

n_queen(0)
print(cnt)
