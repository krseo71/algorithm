# 문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string에 들어있는 각 문자를
# n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.

# def solution(my_string, n):
#     return [n*i for i in my_string]

solution = lambda x, y: ''.join([y * i for i in x])

print(solution("hello", 3))