# BOJ 7511 '소셜 네트워킹 어플리케이션'

import sys
input = sys.stdin.readline

def find(x):
    # 부모 값이 음수 = 자기 자신이 부모
    if network[x] < 0:
        return x
    network[x] = find(network[x])
    return network[x]

def union(x, y):
    # x, y 각각의 부모 찾기
    x = find(x)
    y = find(y)

    # 부모가 같다면 -> 이미 union 된 상태
    if x == y:
        return False
    network[y] = x
    return True

t = int(input())
case = 1

for _ in range(t):
    n = int(input())
    network = [-1] * (n+1)

    # union
    k = int(input())
    for _ in range(k):
        u, v = map(int, input().split())
        union(u, v)

    # find
    print(f'Scenario {case}:')
    m = int(input())
    for _ in range(m):
        u, v = map(int, input().split())
        if find(u) == find(v):
            print(1)
        else:
            print(0)

    case += 1
    print()
