# programmers 42895

def solution(N, number):
    # 최대로 사용 가능한 N의 개수 : 8
    # dp[i] : N을 i번 사용하여 구할 수 있는 숫자들의 집합(중복 방지를 위해 set 사용)
    dp = [set() for _ in range(9)]

    # i : 사용된 N의 개수
    for i in range(1, 9):
        dp[i].add(int(str(N)*i))
        for j in range(1, i):
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
        if number in dp[i]:
            return i

    return -1
