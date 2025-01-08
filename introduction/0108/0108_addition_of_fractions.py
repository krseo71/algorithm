# 첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1,
# 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다.
# 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.
def solution(number1, denom1, number2, denom2):
    g = GCD((number1 * denom2 + number2 * denom1), (denom1 * denom2))
    return [(number1 * denom2 + number2 * denom1) // g , (denom1 * denom2) // g]

def GCD(a, b):
    while(b>0):
        a, b = b, a%b
    return a

print(solution(7, 13, 2, 6))