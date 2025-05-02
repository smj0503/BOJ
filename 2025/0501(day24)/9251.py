# BOJ 9251 'LCS'

str1 = ' ' + input()
str2 = ' ' + input()

dp = [[0] * len(str2) for _ in range(len(str1))]

for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] != str2[j]:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]) + 1

print(dp[-1][-1])
