# BOJ 17609

def is_palindrome(s):
    return s == s[::-1]

def is_pseudo_palindrome(s):
    left, right = 0, len(s)-1

    while left < right:
        if s[left] != s[right]:
            temp1 = s[left+1:right+1]
            temp2 = s[left:right]
            return is_palindrome(temp1) or is_palindrome(temp2)
        left += 1
        right -= 1

    return True

t = int(input())
for _ in range(t):
    string = input()
    if is_palindrome(string):
        print(0)
    elif is_pseudo_palindrome(string):
        print(1)
    else:
        print(2)
