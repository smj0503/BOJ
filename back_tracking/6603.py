# 백준 6603 '로또'
# 로또 번호는 6개

import sys
input = sys.stdin.readline

def func(cur, check, arr, numbers):
    if cur == 6:
        for i in arr:
            print(i, end=' ')
        print()
        return

    for i in range(len(numbers)):
        if not check[i] and (cur == 0 or numbers[i] > arr[-1]):
            arr.append(numbers[i])
            check[i] = True
            func(cur + 1, check, arr, numbers)
            arr.pop()
            check[i] = False

while True:
    test_case = input().strip()
    if test_case == '0':
        break
    else:
        candidates = list(map(int, test_case.split()))
        k = candidates.pop(0)

    isUsed = [False] * k
    pick = []

    func(0, isUsed, pick, candidates)
    print()
