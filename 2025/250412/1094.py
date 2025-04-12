# BOJ 1094

x = int(input())
stack = [64]

while True:
    if sum(stack) == x:
        break

    stick = stack.pop()
    stick //= 2
    stack.append(stick)
    if sum(stack) < x:
        stack.append(stick)

print(len(stack))
