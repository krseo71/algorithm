

def summarize_string(input_str):
    dic = {}
    answer = ''
    for s in input_str:
        if s not in dic:
            dic[s] = 1
        else:
            dic[s] += 1
    for i, j in dic.items():
        answer += str(i)+str(j)+ '/'

    return answer[:-1:]


input_str = "acccdeee"

print(summarize_string(input_str))