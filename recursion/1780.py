# 백준 1780 '종이의 개수'

import sys
input = sys.stdin.readline

N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

# -1, 0, 1 의 개수
cnt = [0, 0, 0]

# 해당 종이 내부에 같은 숫자로만 채워졌는지 확인하는 함수
def check(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[x][y] != paper[i][j]:
                return False
    return True

def func(x, y, z):
    # 만약 같은 숫자로만 채워져 있다면,
    if check(x, y, z):
        # paper[x][y] : 체크 시작 지점의 값(숫자)
        # paper[x][y] = -1 일 경우 index = 0,
        # paper[x][y] = 0  일 경우 index = 1,
        # paper[x][y] = 1  일 경우 index = 2,
        # 따라서 cnt[paper[x][y] + 1] += 1 이라는 수식을 수행.
        cnt[paper[x][y] + 1] += 1
        return

    # 같은 숫자로만 채워져 있지 않다면 -> 9등분
    n = z // 3
    for i in range(3):
        for j in range(3):
            func(x + i * n, y + j * n, n)

func(0, 0, N)
for c in cnt:
    print(c)
