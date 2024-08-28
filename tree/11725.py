# 백준 11725 '트리의 부모 찾기'

from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N = int(input())
tree = [[] for _ in range(N + 1)]
parent = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# BFS 풀이
# def BFS():
#     q = deque([1])
#
#     while q:
#         cur = q.popleft()
#         for node in tree[cur]:
#             if not parent[node]:
#                 parent[node] = cur
#                 q.append(node)

# DFS 재귀 풀이
def DFS(cur):
    for node in tree[cur]:
        if parent[node] == 0:
            parent[node] = cur
            DFS(node)

# DFS 비재귀 풀이
# def DFS(root):
#     stack = deque([root])
#
#     while stack:
#         cur = stack.pop()
#         for node in tree[cur]:
#             if parent[node] == 0:
#                 parent[node] = cur
#                 stack.append(node)

# BFS()
DFS(1)
for i in range(2, N + 1):
    print(parent[i])
