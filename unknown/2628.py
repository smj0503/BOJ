# BOJ 2628 '종이자르기'

import sys
input = sys.stdin.readline

row, col = map(int, input().split())
cut = int(input())

row_cuttings = [0, row]
col_cuttings = [0, col]

for _ in range(cut):
    x, y = map(int, input().split())
    if x == 0:
        col_cuttings.append(y)
    else:
        row_cuttings.append(y)

row_cuttings.sort()
col_cuttings.sort()

ans = 0
for i in range(1, len(row_cuttings)):
    for j in range(len(col_cuttings)):
        width = row_cuttings[i] - row_cuttings[i - 1]
        height = col_cuttings[j] - col_cuttings[j - 1]
        ans = max(ans, width * height)

print(ans)
