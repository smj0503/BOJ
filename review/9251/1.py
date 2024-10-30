# BOJ 9251 'LCS'
# LCS : 최장 공통 부분 수열 (* 부분 수열은 연속된 값이 아니다)

string_A = ' ' + input()
string_B = ' ' + input()

dp = [[0] * len(string_B) for _ in range(len(string_A))]

for i in range(1, len(string_A)):
    for j in range(1, len(string_B)):
        if string_A[i] == string_B[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[-1][-1])
