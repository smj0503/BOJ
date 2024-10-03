# BOJ '지능형 기차 2'

ans = 0
current = 0
for i in range(10):
    off, on = map(int, input().split())
    current -= off
    current += on
    ans = max(ans, current)

print(ans)
