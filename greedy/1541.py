# 백준 1541 '잃어버린 괄호'

exp = input()
arr_exp = exp.split('-')
numbers = []

for i in arr_exp:
    numbers.append(sum(map(int, i.split('+'))))

ans = -(sum(numbers) - numbers[0] * 2)
print(ans)
