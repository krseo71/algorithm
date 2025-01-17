

n = int(input())
heights = list(map(int, input().split()))
def solution(heights):
    stack = [] # 탑의 인덱스와 높이를 저장할 스택
    answer = [0] * len(heights)

    for i in range(len(heights)):
        while stack and stack[-1][1] <= heights[i]:
            stack.pop() # 현재 탑이 더 높다면 스택에서 해당 탑을 제거 -> 스택에 현재 탑보다 높은 탑만 유지됨
        if stack:
            answer[i] = stack[-1][0] + 1
        stack.append([i, heights[i]]) # 현재 탑의 인덱스와 높이를 스택에 추가
    print(*answer)

solution(heights)