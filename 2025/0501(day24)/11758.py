# BOJ 11758 'CCW'

# CCW(Counter Clock Wise) 알고리즘
# 외적을 이용, 2차원 평면 상의 세 점의 진행 방향을 알아내기 위해 사용
# 외적의 z축 결과가 음수면 시계 방향, 0이면 직선, 양수면 반시계 방향

# "신발끈 공식"으로 해결

points = []
for _ in range(3):
    points.append(list(map(int, input().split())))

x1, y1 = points[0]
x2, y2 = points[1]
x3, y3 = points[2]
x4, y4 = points[0]

val = (x1 * y2 + x2 * y3 + x3 * y4) - (x2 * y1 + x3 * y2 + x4 * y3)

# 반시계 방향
if val > 0:
    print(1)
# 시계 방향
elif val < 0:
    print(-1)
# 일직선
else:
    print(0)
