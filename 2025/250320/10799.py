# BOJ 10799 '쇠막대기'

stick = input()
stack = []
answer = 0

for i in range(len(stick)):
    # 열린 괄호일 경우 : stack push
    if stick[i] == '(':
        stack.append(stick[i])
    # 닫힌 괄호일 경우
    else:
        stack.pop()
        # 이전 괄호가 열린 괄호면 = 레이저
        if stick[i-1] == '(':
            answer += len(stack)
        # 이전 괄호가 닫힌 괄호면 = 막대의 끝
        else:
            answer += 1

print(answer)
