# 문자열 my_string, overwrite_string과 정수 s가 주어집니다.
# 문자열 my_string의 인덱스 s부터 overwrite_string의 길이만큼을
# 문자열 overwrite_string으로 바꾼 문자열을 return 하는 solution 함수를 작성해 주세요.

a = "He11oWor1d"
b = "lloWorl"
c = 2
def solution(my_string, overwrite_string, s):
    l = len(overwrite_string)
    s1 = my_string[0:s]
    s2 = my_string[s+l:]

    return s1+overwrite_string+s2

print(solution(a,b,c))