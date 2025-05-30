# BOJ 1717

import sys
input = sys.stdin.readline

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

n, m = map(int, input().split())
parent = [-1] * (n+1)

for _ in range(m):
    op, u, v = map(int, input().split())
    if op == 0:
        union(u, v)
    else:
        if find(u) == find(v):
            print('YES')
        else:
            print('NO')
