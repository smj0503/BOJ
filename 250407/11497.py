import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    ans = 0
    for i in range(2, n):
        ans = max(ans, abs(arr[i] - arr[i-2]))

    print(ans)
