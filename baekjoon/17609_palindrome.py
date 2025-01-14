# 팰린드롬 확인 함수
def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:  # 좌우 문자가 다르면 팰린드롬이 아님
            return False
        left += 1
        right -= 1
    return True

# 팰린드롬 유형 확인 함수
def palindrome_type(s):
    left = 0
    right = len(s) - 1
    while left < right:  # 양 끝에서부터 중앙으로 이동하며 비교
        if s[left] != s[right]:  # 좌우 문자가 다르면
            # 왼쪽 문자를 제거한 경우 또는 오른쪽 문자를 제거한 경우 팰린드롬인지 확인
            if is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1):
                return 1  # 유사 팰린드롬
            else:
                return 2  # 팰린드롬 X
        left += 1
        right -= 1

    return 0  # 완전한 팰린드롬

n = int(input())
for _ in range(n):
    s = input().strip()
    print(palindrome_type(s))




# print(is_palindrome("abba")) abba summuus xabba xabbay
# print(is_palindrome("summuus"))
# print(is_palindrome("xabba"))
# print(is_palindrome("xabbay"))
# print(is_palindrome("comcom"))
# print(is_palindrome("comwwmoc"))
# print(is_palindrome("comwwtmoc"))
