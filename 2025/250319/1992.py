# BOJ 1992 '쿼드트리'

N = int(input())
quad = []
result = ''

for _ in range(N):
    quad.append(list(input()))

def check(x, y, gap):
    for i in range(x, x + gap):
        for j in range(y, y + gap):
            if quad[x][y] != quad[i][j]:
                return False
    return True

def dfs(x, y, gap):
    global result
    if check(x, y, gap):
        result += quad[x][y]
        return

    result += '('
    gap = gap // 2
    for i in range(2):
        for j in range(2):
            dfs(x + i * gap, y + j * gap, gap)
    result += ')'

dfs(0, 0, N)
print(result)
