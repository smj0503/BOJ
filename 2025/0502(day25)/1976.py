# BOJ 1976 '여행 가자'

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
travel = list(map(int, input().split()))

parent = [-1] * n

def find(x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False
    parent[y] = x
    return True

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and find(i) != find(j):
            union(i, j)

possible = 'YES'
for i in range(1, m):
    if find(travel[i]-1) != find(travel[i-1]-1):
        possible = 'NO'
        break

print(possible)
