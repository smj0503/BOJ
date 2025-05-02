# BOJ 17609 '회문'

# palindrome 체크 함수: 시간 복잡도 O(n)
def is_palindrome(s):
    return s == s[::-1]

def is_pseudo_palindrome(s):
    # 양쪽 포인터 초기화(양끝)
    left, right = 0, len(s) - 1

    while left < right:
        # 양쪽 문자 다르면 -> 문자 하나 삭제 후 회문인지 검사
        if s[left] != s[right]:
            temp1 = s[left+1:right+1]    # 왼쪽 문자 하나 제거: s[left+1:right+1]
            temp2 = s[left:right]        # 오른쪽 문자 하나 제거: s[left:right]
            return is_palindrome(temp1) or is_palindrome(temp2)
        # 양쪽 문자 같으면 -> 포인터 한칸씩 안쪽 이동
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
