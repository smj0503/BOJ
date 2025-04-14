# BOJ 1789

S = int(input())

ans = 1
while True:
    S -= ans
    if S <= ans:
        break
    ans += 1

print(ans)
