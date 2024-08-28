# 백준 18870 '좌표 압축'

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# 파이썬 set은 중복 허용 x. 따라서
# 1. 입력 받은 list를 set으로 변경
# 2. 변경한 set을 다시 list로 변경
# 3. 변경된(중복 제거된) list를 sort(정렬)
arr_sorted = sorted(set(arr))
dic = {}

# arr_sorted (arr을 정렬 및 중복 제거한 상태)의 각 요소의 인덱스 값이
# 곧 해당 요소 보다 값이 작은 요소의 개수 이다.
for i in range(len(arr_sorted)):
    dic[arr_sorted[i]] = i

for x in arr:
    print(dic[x], end = " ")
