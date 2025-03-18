# BOJ 10799 '쇠막대기'

s = input()
stack = []
count = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    else:
        if s[i-1] == '(':
            stack.pop()
            count += len(stack)
        else:
            stack.pop()
            count += 1

print(count)
