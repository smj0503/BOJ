# BOJ 11053 '가장 긴 증가하는 부분 수열' (LIS)

# 핵심
# 1. 원소 arr[i]는 arr[i]전의 원소 arr[k] (0 <= k < i) 중 어떤 arr[k] 뒤에 올 수 있는가?
# 2. arr[i]에 대해 arr[i] 앞에 올 수 있는 원소의 개수를 관리할 수 있으면 된다.

# DP 구현 방법
# 1. dp[i] : arr[i]까지의 LIS 길이를 저장하는 배열
# 2. dp[i]의 마지막 원소는 arr[i]
# 3. 그렇다면 dp[i]는 dp[k]의 (0 < k < i, arr[k] <= arr[i]) 최댓값 +1이 된다.
# 4. 즉, arr[i]를 마지막 원소로 하는 LIS 길이는, arr[0]부터 arr[i-1] 중 arr[i]보다 작은
#    원소들에 대해 그들을 마지막 원소로 가지는 LIS 길이에 1을 더한 것이다.
# 5. arr[i]를 맨 뒤에 붙일 수 있는지 없는지를 따지면서 최댓값을 갱신해 나간다.

n = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
