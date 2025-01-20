# 알파벳 대문자로 이루어진 문자열을 입력받아 같은 문자가 연속으로 반복되는 경우 반복되는
# 문자 바로 오른쪽에 반복 횟수를 표기하는 방법으로 문자열을 압축하는 프로그램을 작성하시오.
# 단 반복횟수가 1인 경우 생략합니다.

string = 'KSTTTSEEKFKKKDJJGG'
# string = input()
def solution(s):
    a = ""
    answer = ""
    cnt = 1
    for i in s:
        if a != i:
            if cnt != 1:
                answer += str(cnt) + i
                cnt = 1
            else:
                answer += i
        else:
            cnt += 1
        a = i
    print(answer + str(cnt))

solution(string)

# KST3SE2KFK3DJ2G2
# KST3SE2KFK3DJ2G