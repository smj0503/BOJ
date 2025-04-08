# BOJ 9663 'N-QUEEN'

# [접근 포인트]
# 0. 한 행에는 하나의 Queen만 놓일 수 있으므로 같은 행일 경우는 고려x
# 1. 같은 열에 위치 하는지를 확인 하려면? -> y좌표가 일치 하는지를 확인
# 2. 같은 /(우상향) 대각선 위에 위치 하는지를 확인 하려면? -> x + y 값이 일치 하는지를 확인
# 3. 같은 \(우하향) 대각선 위에 위치 하는지를 확인 하려면? -> x - y 값이 일치 하는지를 확인

# 1, 2, 3 각각에 대응되는 isUsed1, isUsed2, isUsed3 배열을 생성.
# isUsed1 : (x, y)에 퀸이 있으면 isUsed1[y] = True            (배열 크기 : n)
# isUsed2 : (x, y)에 퀸이 있으면 isUsed2[x+y] = True          (배열 크기 : 2n - 1)
# isUsed3 : (x, y)에 퀸이 있으면 isUsed3[(x-y)+(n-1)] = True  (배열 크기 : 2n - 1)

n = int(input())
cnt = 0

is_used1 = [0] * n
is_used2 = [0] * (2*n-1)
is_used3 = [0] * (2*n-1)

def dfs(cur):
    global cnt
    if cur == n:
        cnt += 1
        return

    # 만약, (cur, i)에 퀸을 둘 수 있다면, (cur = x좌표, i = y좌표)
    # is_used1[i], is_used2[cur+i}, is_used3[(cur-i) + (n-1)] 값을 1(true)로 변한 후 dfs(cur+1)을 호출
    for i in range(n):
        if not is_used1[i] and not is_used2[cur+i] and not is_used3[(cur-i) + (n-1)]:
            is_used1[i] = 1
            is_used2[cur+i] = 1
            is_used3[(cur-i) + (n-1)] = 1
            dfs(cur+1)
            is_used1[i] = 0
            is_used2[cur+i] = 0
            is_used3[(cur-i) + (n-1)] = 0

dfs(0)
print(cnt)
