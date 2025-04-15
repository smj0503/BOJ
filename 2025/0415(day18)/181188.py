# PROGRAMMERS 181188 '요격 시스템'

targets = [[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]]
targets.sort(key = lambda x : x[1])

answer = 0
start = end = 0

for x, y in targets:
    if x >= end:
        answer += 1
        end = y

print(answer)
