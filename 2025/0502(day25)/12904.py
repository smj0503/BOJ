# BOJ 12904 'A와 B'

s = input()
t = input()

n = len(t) - len(s)
for _ in range(n):
    if t[-1] == 'A':
        t = t[:-1]
    else:
        t = t[:-1]
        t = t[::-1]

if t == s:
    print(1)
else:
    print(0)
