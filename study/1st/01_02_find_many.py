def find_max_occurred_alphabet(string):
    dic = dict()
    for s in string:
        if s.isalpha():
            dic[s] = string.count(s)
    print(dic)

    m = max(dic.values())
    if list(dic.values()).count(m) != 1:
        return -1
    for key, value in dic.items():
        if value == m:
            return key


result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))