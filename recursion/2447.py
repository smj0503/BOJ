# 백준 2447 '별 찍기 - 10'

N = int(input())
graph = ['***', '* *', '***']

def func(n, arr):
    if n == N:
        for line in arr:
            print(line)
        return

    next = []
    # 전체 그림을 가로로 3등분 한다고 가정할 때,
    # 위에서 부터 첫번째 가로 줄
    for i in range(n):
        next.append(arr[i] * 3)
    # 위에서 부터 두번째 가로 줄
    for i in range(n):
        next.append(arr[i] + ' ' * n + arr[i])
    # 위에서 부터 세번째 가로 줄
    for i in range(n):
        next.append(arr[i] * 3)

    return func(n * 3, next)

func(3, graph)
