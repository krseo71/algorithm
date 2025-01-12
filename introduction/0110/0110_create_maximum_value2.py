# 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

def solution(numbers):
    n = len(numbers)
    s = 1
    answer = -100000000
    for number in numbers:
        for i in range(s, n):
            if answer < numbers[i] * number:
                answer = numbers[i] * number
        s += 1
    return answer
solution([-2])