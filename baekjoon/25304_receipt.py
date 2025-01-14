X = int(input()) # 총 예산
N = int(input()) # 구매한 품목의 개수

def solution(X, N):
    sum = 0
    for i in range(N):
        a, b = map(int, input().split())
        sum += a * b

    if sum == X:
        return 'Yes'

    return 'No'

print(solution(X, N))



