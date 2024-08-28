# 백준 2557 '숫자의 개수'

A = int(input())
B = int(input())
C = int(input())

mul = str(A*B*C)

count = [0] * 10

for m in mul:
    idx = int(m)
    count[idx] += 1

for c in count:
    print(c)
