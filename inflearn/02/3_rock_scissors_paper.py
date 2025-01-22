N = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

def solution(arr1, arr2, n):
    answer = []
    for i in range(n):
        if arr1[i] == 1:
            if arr2[i] == 1:
                answer.append("D")
            elif arr2[i] == 2:
                answer.append("B")
            else:
                answer.append("A")
        elif arr1[i] == 2:
            if arr2[i] == 1:
                answer.append("A")
            elif arr2[i] == 2:
                answer.append("D")
            else:
                answer.append("B")
        else:
            if arr2[i] == 1:
                answer.append("B")
            elif arr2[i] == 2:
                answer.append("A")
            else:
                answer.append("D")

    return print(*answer, sep="\n")

solution(arr1, arr2, N)