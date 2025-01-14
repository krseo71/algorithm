input = "abadabac"

def find_not_repeating_first_character(string):
    dic = dict()
    for s in string:
        if s not in dic:
            dic[s] = 1
        else:
            dic[s] += 1
    for d, i in dic.items():
        if i == 1:
            return d
    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))