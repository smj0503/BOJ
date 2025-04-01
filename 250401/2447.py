# BOJ 2447
# 3등분
# 상/중/하 나눠서 접근

N = int(input())
graph = ['***', '* *', '***']

def dfs(n, pic):
    if n == N:
        for p in pic:
            print(p)
        return

    new_pic = []
    for i in range(n):
        new_pic.append(pic[i] * 3)
    for i in range(n):
        new_pic.append(pic[i] + ' ' * n + pic[i])
    for i in range(n):
        new_pic.append(pic[i] * 3)

    return dfs(n * 3, new_pic)

dfs(3, graph)
