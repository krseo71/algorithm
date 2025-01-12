# 정수 배열 arr가 주어집니다. 배열 안의 2가 모두 포함된 가장 작은 연속된
# 부분 배열을 return 하는 solution 함수를 완성해 주세요.
# 단, arr에 2가 없는 경우 [-1]을 return 합니다.

def solution(arr):
    if 2 not in arr:
        return [-1]
    s = arr[:]
    e = arr[:][::-1]
    a = s.index(2) # a
    b = e.index(2) # n-(b+1)
    return arr[a:len(arr)-b]



print(solution([1,1,1]))
print(solution([1, 2, 1, 4, 5, 2, 9]))
print(solution([1, 2, 1]))
