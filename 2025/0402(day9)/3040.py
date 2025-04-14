# BOJ 3040

from itertools import combinations

dwarfs = [int(input()) for _ in range(9)]
total_sum = sum(dwarfs)

for i, j in combinations(range(9), 2):
    if total_sum - dwarfs[i] - dwarfs[j] == 100:
        for x in range(9):
            if x not in [i, j]:
                print(dwarfs[x])
