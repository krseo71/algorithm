# 영어 알파벳과 특수문자로 구성된 문자열이 주어지면 영어 알파벳만 뒤집고,
# 특수문자는 자기 자리에 그대로 있는 문자열을 만들어 출력하는 프로그램을 작성하세요.

# s = 'a#b!GE*T@S'
s = input()
s = list(s)
lt = 0
rt = len(s) -1

while lt < rt:
    if not s[lt].isalpha():
        lt += 1
    elif not s[rt].isalpha():
        rt -= 1
    else:
        s[lt], s[rt] = s[rt], s[lt]
        lt += 1
        rt -= 1

print(''.join(s))







