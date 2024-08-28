# 백준 1475 '방 번호'

num = input()
count = [0] * 10

for n in num:
    if n == '6' or n == '9':
        if count[6] == count[9]:
            count[6] += 1
        else:
            count[9] += 1
    else:
        count[int(n)] += 1

print(max(count))
