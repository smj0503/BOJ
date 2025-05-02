# BOJ 7511

import sys
input = sys.stdin.readline

def find(x):
    if network[x] < 0:
        return x
    network[x] = find(network[x])
    return network[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False
    network[y] = x
    return True

t = int(input())
case = 1

for _ in range(t):
    n = int(input())
    network = [-1] * (n+1)

    # k: union 횟수
    k = int(input())
    for _ in range(k):
        a, b = map(int, input().split())
        union(a, b)

    # m: find 횟수
    print(f'Scenario {case}:')
    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if find(a) == find(b):
            print(1)
        else:
            print(0)

    print()
    case += 1
