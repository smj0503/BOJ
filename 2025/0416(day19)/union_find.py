parent = [-1] * 10

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
