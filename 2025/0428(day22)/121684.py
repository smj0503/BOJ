# PROGRAMMERS 121684 '체육대회'

ability = [[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]

# count : 대표가 뽑힌 종목의 수
# total : 능력치 총합
def dfs(count, total, ability, is_selected):
    global answer
    # 학생 수
    n = len(ability)
    # 종목 수
    m = len(ability[0])

    if count == m:
        answer = max(answer, total)
        return

    for i in range(n):
        if not is_selected[i]:
            is_selected[i] = 1
            dfs(count+1, total + ability[i][count], ability, is_selected)
            is_selected[i] = 0

def solution(ability):
    global answer
    answer = 0

    # 학생 별 선발 여부
    is_selected = [0] * len(ability)
    dfs(0, 0, ability, is_selected)

    return answer
