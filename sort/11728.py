# 백준 11728번 '배열 합치기'
# 정렬

N, M = map(int, input().split())

arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

arrA.sort()
arrB.sort()

arrC = arrA + arrB
arrC.sort()

for c in arrC:
    print(c, end=' ')
