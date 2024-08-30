# BOJ 2812 '크게 만들기'

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num = input().strip()

stack = []
for n in num:
    # 스택에 가장 최근에 들어온 값과 새로 들어온 값을 비교
    # 스택에 들어 있는 값이 더 작으면 pop
    while stack and stack[-1] < n and K > 0:
        stack.pop()
        K -= 1
    stack.append(n)

# 여기서 주의할 점!
# 앞에서부터 비교해 나가기 때문에, 비교가 끝난 시점에 K > 0 일수도 있다.
# 이를 고려해서 출력을 경우에 따라 다르게 해줘야 한다.
print(''.join(stack[:len(stack) - K]))
