# 길이가 같은 두 문자열 str1과 str2가 주어집니다.
# 두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 return 하는 solution 함수를 완성해 주세요.

a = "aaaaa"
b = "bbbbb"
def solution(str1, str2):
    list = []
    for i in range(len(str1)):
        list.append(str1[i])
        list.append(str2[i])
    return ''.join(list)

print(solution(a,b))