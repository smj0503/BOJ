# BOJ 1789 '수들의 합'

S = int(input())
i = 1

while True:
    S -= i
    if S == 0:
        print(i)
        break
    else:
        if S <= i:
            print(i)
            break
        else:
            i += 1
