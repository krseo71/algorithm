# 정수 배열 arr이 매개변수로 주어집니다. arr의 길이가 2의 정수 거듭제곱이 되도록 arr 뒤에 정수 0을 추가하려고 합니다.
# arr에 최소한의 개수로 0을 추가한 배열을 return 하는 solution 함수를 작성해 주세요.

def solution(arr):
    n = len(arr)
    a = 0
    for i in range(1, n):
        if 2**i > n:
            a = i
            break
        elif 2**i == n:
            return arr
    b = 2**a - n
    for i in range(b):
        arr.append(0)

    return arr


solution([1,2,3,4,5,6,7,8,9])

