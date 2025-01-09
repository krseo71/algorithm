# 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 정수 배열 array가 매개변수로 주어질 때,
# 최빈값을 return 하도록 solution 함수를 완성해보세요. 최빈값이 여러 개면 -1을 return 합니다.

def solution(array):
    dic = {}
    for i in array:
        dic[i] = array.count(i)

    m = max(dic.values())
    if list(dic.values()).count(m) != 1:
        return -1

    for key, value in dic.items():
        if value == m:
            return key

solution([1,2,3,3,3,4,5,6,6,6])