# BOJ 2578 '빙고'

plate = []
numbers = []

# 빙고판 입력 받기
for _ in range(5):
    plate.append(list(map(int, input().split())))

# 사회자가 부르는 숫자 -> 주의할 점 ! : 1차원 배열로 받기(extend)
for _ in range(5):
    numbers.extend(map(int, input().split()))

bingo = 0

# 중복 방지 체크 배열
rowChecked = [False] * 5
colChecked = [False] * 5
increaseCrossChecked = False
decreaseCrossChecked = False

# 가로 빙고 체크
def checkRow():
    global bingo
    for i in range(5):
        if not rowChecked[i] and plate[i][0] == plate[i][1] == plate[i][2] == plate[i][3] == plate[i][4] == 'x':
            bingo += 1
            rowChecked[i] = True

# 세로 빙고 체크
def checkCol():
    global bingo
    for i in range(5):
        if not colChecked[i] and plate[0][i] == plate[1][i] == plate[2][i] == plate[3][i] == plate[4][i] == 'x':
            bingo += 1
            colChecked[i] = True

# 우상향 대각선 체크
def checkIncreaseCross():
    global bingo
    global increaseCrossChecked

    if not increaseCrossChecked and plate[0][4] == plate[1][3] == plate[2][2] == plate[3][1] == plate[4][0] == 'x':
        bingo += 1
        increaseCrossChecked = True

# 우하향 대각선 체크
def checkDecreaseCross():
    global bingo
    global decreaseCrossChecked

    if not decreaseCrossChecked and plate[0][0] == plate[1][1] == plate[2][2] == plate[3][3] == plate[4][4] == 'x':
        bingo += 1
        decreaseCrossChecked = True

for k in range(25):
    call = numbers[k]

    # 불려진 숫자에 x 표시
    for i in range(5):
        for j in range(5):
            if plate[i][j] == call:
                plate[i][j] = 'x'

    checkRow()
    checkCol()
    checkIncreaseCross()
    checkDecreaseCross()

    if bingo >= 3:
        print(k + 1)
        break
