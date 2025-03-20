# BOJ 9012 '괄호'

def check_is_vps(target):
    flag = 0
    for t in target:
        if t == '(':
            flag += 1
        else:
            flag -= 1

        if flag < 0:
            print('NO')
            return

    if flag == 0:
        print('YES')
    else:
        print('NO')

T = int(input())
for _ in range(T):
    string = input()
    check_is_vps(string)
