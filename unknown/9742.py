# BOJ 9742 '순열'

import itertools

a, b = map(str, input().split())
letters = list(a)
b = int(b)
perms = list(itertools.permutations(letters))

if b <= len(perms):
    print(a, b, '=', ''.join(perms[b-1]))
else:
    print("No permutation")
