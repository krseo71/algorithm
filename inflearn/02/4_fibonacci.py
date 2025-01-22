N = int(input())

def solution(n):
    if n == 1 or n == 2:
        return 1
    return solution(n-1) + solution(n-2)


arr = []
for i in range(N):
    arr.append(solution(N))
print(arr)
