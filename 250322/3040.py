# BOJ 3040 '백설 공주와 일곱 난쟁이'

dwarfs = [int(input()) for _ in range(9)]
sum_dwarfs = sum(dwarfs)
x, y = 0, 0

for i in range(9):
    for j in range(i + 1, 9):
        if sum_dwarfs - dwarfs[i] - dwarfs[j] == 100:
            for k in range(9):
                if k not in [i, j]:
                    print(dwarfs[k])
