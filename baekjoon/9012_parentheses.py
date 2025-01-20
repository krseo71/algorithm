
def solution(s):
    stack = []
    arr = list(s)
    for a in arr:
        if a == '(':
            stack.append(a) # 여는 괄호를 만나면 스택에 추가
        elif a == ')':
            if not stack:
                return "NO" # 스택이 비어있다면 NO
            stack.pop() # 닫는 괄호를 만나면 스택에서 제거

    # 모든 문자를 처리한 후 스택이 비어있어야 올바른 괄호 문자열
    return "YES" if not stack else "NO"

N = int(input())
for _ in range(N):
    print(solution(input()))