# BOJ 1991 '트리 순회'

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n = int(input())
tree = {}

for _ in range(n):
    root, lc, rc = map(str, input().split())
    tree[root] = lc, rc

# 전위 : root -> lc -> rc
def preorder(node):
    if node != '.':
        print(node, end='')
        preorder(tree[node][0])
        preorder(tree[node][1])


# 중위 : lc -> root -> rc
def inorder(node):
    if node != '.':
        inorder(tree[node][0])
        print(node, end='')
        inorder(tree[node][1])

# 후위 : lc -> rc -> root
def postorder(node):
    if node != '.':
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
