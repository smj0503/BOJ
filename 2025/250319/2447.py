# BOJ 2447 '별 찍기 - 10'

N = int(input())
graph = ['***', '* *', '***']

def dfs(n, arr):
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

    return dfs(n * 3, new_arr)

dfs(3, graph)
