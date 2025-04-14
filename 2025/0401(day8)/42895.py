# 프로그래머스 42895

def solution(N, number):
    if N == number:
        return 1

    answer = -1
    dp = [set() for _ in range(8)]

    # N = 3일 경우, 3, 33, 333, ..., 33333333 추가
    for i in range(8):
        dp[i].add(int(str(N) * (i + 1)))

    for i in range(1, 8):
        for j in range(i):
            for op1 in dp[j]:
                for op2 in dp[i-j-1]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)

        if number in dp[i]:
            answer = i + 1
            break

    return answer

result = solution(5, 12)
print(result)
