#정수가 담긴 리스트 num_list가 주어집니다. num_list의 홀수만 순서대로 이어 붙인 수와
#짝수만 순서대로 이어 붙인 수의 합을 return하도록 solution 함수를 완성해주세요.
from numbers import Number


def solution(num_list):
    even = ''
    odd = ''
    for i in num_list:
        if i % 2 == 0:
            even += str(i)
        else:
            odd += str(i)
    return int(even) + int(odd)


list1 = [3,4,5,2,1]
solution(list1)