# 백준 2447 '별 찍기 - 11'

N = int(input())
graph = ['  *  ', ' * * ', '*****']

def func(n, arr):
    if n == N:
        for line in arr:
            print(line)

    next = []
    
