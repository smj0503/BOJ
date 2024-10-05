# BOJ 2839 '설탕 배달'

# N = int(input())
# dp = [-1] * 5001
# dp[3] = 1
# dp[5] = 1
#
# if N <= 5:
#     print(dp[N])
# else:
#     for i in range(6, N + 1):
#         # i = 홀수
#         if i % 2 == 1:
#             for j in range(1, (i + 1) // 2):
#                 if dp[j] != -1 and dp[i - j] != -1:
#                     count = dp[j] + dp[i - j]
#                     if dp[i] > 0:
#                         dp[i] = min(count, dp[i])
#                     else:
#                         dp[i] = count
#         # i = 짝수
#         else:
#             for j in range(1, (i + 1) // 2 + 1):
#                 if dp[j] != -1 and dp[i - j] != -1:
#                     count = dp[j] + dp[i - j]
#                     if dp[i] > 0:
#                         dp[i] = min(count, dp[i])
#                     else:
#                         dp[i] = count
#     print(dp[N])

# 다른 풀이 (better)
N = int(input())

if N % 5 == 0:  # 5으로 나누어 떨어질 때
    print(N // 5)
else:
    bag = 0
    while N > 0:
        N -= 3
        bag += 1
        if N % 5 == 0:  # 3kg과 5kg를 조합해서 담을 수 있을 때
            bag += N // 5
            print(bag)
            break
        elif N == 1 or N == 2:  # 설탕 봉지만으로 나눌 수 없을 때
            print(-1)
            break
        elif N == 0:  # 3으로 나눠떨어질 때
            print(bag)
            break
