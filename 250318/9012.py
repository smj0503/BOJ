# BOJ 9012 '괄호'

T = int(input())

def check_is_vps(target):
    stack = []
    for t in target:
        if t == '(':
            stack.append(t)
        else:
            if len(stack) == 0:
                print('NO')
                return
            stack.pop()

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')

for _ in range(T):
    string = input()
    check_is_vps(string)
