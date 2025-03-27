# BOJ 3040

dwarfs = [int(input()) for _ in range(9)]
target1, target2 = -1, -1

for i in range(9):
    for j in range(i + 1, 9):
        if sum(dwarfs) - dwarfs[i] - dwarfs[j] == 100:
            target1, target2 = dwarfs[i], dwarfs[j]

dwarfs.remove(target1)
dwarfs.remove(target2)

for d in dwarfs:
    print(d)
