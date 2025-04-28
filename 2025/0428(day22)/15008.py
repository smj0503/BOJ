# PROGRAMMERS 15008 '외톨이 알파벳'

input_string = input()
answer = []
counts = {input_string[0]: 1}
n = len(input_string)

for i in range(1, n):
    if input_string[i] != input_string[i-1]:
        if input_string[i] not in counts:
            counts[input_string[i]] = 1
        else:
            counts[input_string[i]] += 1

for c in counts:
    if counts[c] > 1:
        answer.append(c)

if len(answer) == 0:
    answer = 'N'
else:
    answer.sort()
    answer = ''.join(answer)
