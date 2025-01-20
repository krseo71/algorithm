# 소문자로 된 한개의 문자열이 입력되면 중복된 문자를 제거하고 출력하는 프로그램을 작성하세요.
# 중복이 제거된 문자열의 각 문자는 원래 문자열의 순서를 유지합니다.


a = 'ksekkset'
dic = dict()
for i in a:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

answer = [i for i in dic]
print(''.join(answer))

