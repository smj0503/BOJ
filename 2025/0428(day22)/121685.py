# PROGRAMMERS 121684 '유전법칙'

def mendel_peas(gen, order):
    if gen == 1:
        return 'Rr'

    parent = mendel_peas(gen-1, (order-1) // 4 + 1)
    if parent == 'RR' or parent == 'rr':
        return parent

    if order % 4 == 0:
        return 'rr'
    elif order % 4 == 1:
        return 'RR'
    else:
        return 'Rr'

def solution(queries):
    answer = []
    for x, y in queries:
        answer.append(mendel_peas(x, y))
    return answer
