# 정수 배열 array가 매개변수로 주어질 때,
# 가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

def solution(array):
    a = enumerate(array)
    return sorted(list(max(list(a), key=lambda x: x[1])), reverse=True)

print(solution([1, 8, 3]))

# solution = lambda n: sorted(list(max(list(enumerate(n)), key=lambda x: x[1])), reverse=True)