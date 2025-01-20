N = int(input())
array = list(map(int, input().split()))

def solution(array):
    answer = [array[0]]
    for i in range(1, len(array)):
        if array[i] > array[i - 1]:
            answer.append(array[i])

    return answer

print(*solution(array))