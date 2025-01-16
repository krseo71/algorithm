# 한 개의 문자열 s와 문자 t가 주어지면 문자열 s의 각 문자가 문자 t와 떨어진 최소거리를 출력하는 프로그램을 작성하세요.

# a, b = map(str, input().split())
# a, b = 'teachermode', 'e'
a, b = 'fkdgkjdflkgjljslgjkfldjlkfdg', 'f'
def solution(a, b):
    lt = [0] * len(a)
    rt = [0] * len(a)
    index = 0
    point = 1000
    for s in a:
        if s != b:
            lt[index] += 1 + point
            point = lt[index]
        elif s == b:
            lt[index] = 0
            point = 0
        index += 1

    point = 1000
    index = len(a) -1
    for s in a[::-1]:
        if s != b:
            rt[index] += 1 + point
            point = rt[index]
        elif s == b:
            rt[index] = 0
            point = 0
        index -= 1

    print(lt)
    print(rt)
    answer = []
    for i in range(len(a)):
        if lt[i] <= rt[i]:
            answer.append(lt[i])
        else:
            answer.append(rt[i])
    for i in answer:
        print(i, end=' ')

solution(a, b)