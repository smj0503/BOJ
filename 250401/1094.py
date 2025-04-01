# BOJ 1094 '막대기'

x = int(input())
stack = [64]

while True:
    if x == 64:
        break
    stick = stack.pop()
    stick //= 2
    stack.append(stick)

    if sum(stack) < x:
        stack.append(stick)

    if sum(stack) == x:
        break

print(len(stack))
