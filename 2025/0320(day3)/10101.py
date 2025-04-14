# BOJ 10101 '삼각형 외우기'

triangle = 0
ang_cnt = {}
for _ in range(3):
    angle = int(input())
    triangle += angle
    if angle in ang_cnt:
        ang_cnt[angle] += 1
    else:
        ang_cnt[angle] = 1

if triangle == 180:
    if len(ang_cnt) == 1:
        print('Equilateral')
    elif len(ang_cnt) == 2:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')
