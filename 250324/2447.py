# BOJ 2447 '별 찍기 - 10'

N = int(input())

# 초기 값 세팅
graph = ['***', '* *', '***']

def dfs(n, arr):
    # 재귀 종료 조건 설정
    if n == N:
        for line in arr:
            print(line)
        return

    new_arr = []
    for i in range(n):
        new_arr.append(arr[i] * 3)
    for i in range(n):
        new_arr.append(arr[i] + ' ' * n + arr[i])
    for i in range(n):
        new_arr.append(arr[i] * 3)

    # 재귀
    return dfs(3 * n, new_arr)

dfs(3, graph)
