# BOJ 2447

n = int(input())
graph = ['***', '* *', '***']

def func(arr, x):
    if x == n:
        for line in arr:
            print(line)
        return

    new_arr = []
    for line in arr:
        new_arr.append(line * 3)
    for line in arr:
        new_arr.append(line + ' ' * x + line)
    for line in arr:
        new_arr.append(line * 3)

    return func(new_arr, x * 3)

func(graph, 3)
