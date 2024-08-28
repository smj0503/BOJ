# 백준 1919 '애너그램 만들기'

word1 = input()
word2 = input()

alp1 = [0] * 26
alp2 = [0] * 26

for w in word1:
    alp1[ord(w) - 97] += 1

for w in word2:
    alp2[ord(w) - 97] += 1

ans = 0
for i in range(26):
    ans += abs(alp1[i] - alp2[i])

print(ans)
