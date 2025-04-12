# BOJ 10799

stick = input()
stack = []
ans = 0

for i in range(len(stick)):
    if stick[i] == '(':
        stack.append(stick[i])
    else:
        stack.pop()
        if stick[i-1] == '(':
            ans += len(stack)
        else:
            ans += 1

print(ans)
