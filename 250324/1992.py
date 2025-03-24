# BOJ 1992 '쿼드트리'

N = int(input())
quad = []
answer = ''

for _ in range(N):
    quad.append(list(input()))

def check(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            if quad[i][j] != quad[x][y]:
                return False
    return True

def dfs(x, y, n):
    global answer
    if check(x, y, n):
        answer += quad[x][y]
        return

    answer += '('
    n = n // 2
    # 가로 2, 세로 2씩 나누면 토탈 4등분 이므로, 2*2 이중 for문 돌리기
    for i in range(2):
        for j in range(2):
            dfs(x + i*n, y + j*n, n)
    answer += ')'

dfs(0, 0, N)
print(answer)
