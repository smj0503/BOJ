# BOJ 10799

sticks = input()
cnt = 0
stack = []

for i in range(len(sticks)):
    if sticks[i] == '(':
        stack.append(sticks[i])
    else:
        stack.pop()
        # 레이저
        if sticks[i - 1] == '(':
            cnt += len(stack)
        # 막대의 끝
        else:
            cnt += 1

print(cnt)
