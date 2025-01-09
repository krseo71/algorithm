# 문자열 my_string과 정수 s, e가 매개변수로 주어질 때,
# my_string에서 인덱스 s부터 인덱스 e까지를 뒤집은 문자열을 return 하는 solution 함수를 작성해 주세요.

def solution(my_string, s, e):
    a = my_string[s:e+1]
    b = ''
    for i in range(len(a)-1, -1, -1):
        b += list(a)[i]

    return my_string[:s] + b + my_string[e+1:]

solution("Progra21Sremm3",6,12)