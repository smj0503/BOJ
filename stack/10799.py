stick = input()
stack = []
count = 0

for i in range(len(stick)):
  if stick[i] == '(':
    stack.append(stick[i])
  elif stick[i] == ')':
    if stick[i-1] == '(':
      stack.pop()
      count += len(stack)
    elif stick[i-1] == ')':
      stack.pop()
      count += 1

print(count)
