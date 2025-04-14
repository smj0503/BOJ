# BOJ 9084

# 일반적인 경우로 확장해서 생각해보면,
# 2원으로 X원을 만들 수 있는 가지수가 몇 가지인지를 알고 싶다면,
# 2원으로 (X-2)원을 만들 수 있는 가지수가 몇 가지인지 살펴보면 된다.
# 2원으로 X-2원을 만들 수 있는 가지수는, (X-2)+2원(X원)의 가지수와 같다.

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    dp = [0] * (m+1)
    dp[0] = 1

    for coin in coins:
        for i in range(1, m+1):
            if i >= coin:
                dp[i] += dp[i - coin]

    print(dp[m])
