# 양의 정수 n이 매개변수로 주어질 때, n이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 하고
# n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 하는 solution 함수를 작성해 주세요.
list = []
def solution(n):
    if n % 2 == 1:
        if n < 0:
            return
        list.append(n)
        solution(n-2)
    else:
        if n < 0:
            return
        list.append(n*n)
        solution(n-2)
    answer = 0
    for i in list:
        answer += i

    return answer

# print(solution(7))
print(solution(10))