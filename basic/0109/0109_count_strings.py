# 문자열 myString과 pat이 주어집니다. myString에서 pat이 등장하는 횟수를 return 하는 solution 함수를 완성해 주세요.

def solution(myString, pat):
    n = len(pat)
    m = len(myString)
    l = []
    for i in range(m-n + 1):
        l.append(myString[i:i+n])
    return l.count(pat)




k = solution("aaaa","aa")
print(k)