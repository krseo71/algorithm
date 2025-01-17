from collections import deque

n = int(input())

def solution(n):
    k = n // 4 # n을 4로 나눈 몫을 구하여, long을 몇 번 추가할지 결정
    answer = deque(['int'])
    for i in range(k):
        answer.appendleft('long') # long을 앞쪽에 추가
    return ' '.join(answer)

print(solution(n))
