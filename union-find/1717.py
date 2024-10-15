# BOJ 1717 '집합의 표현'

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x, y):
    a = find_parent(x)
    b = find_parent(y)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    operation, a, b = map(int, input().split())
    if operation == 0:
        union_parent(a, b)
    else:
        if find_parent(a) == find_parent(b):
            print('YES')
        else:
            print('NO')
