N = int(input())
arr = list(map(int, input().split()))

def solution(arr):
    cnt = 0
    heights = 0
    for i in arr:
        if i > heights:
            cnt += 1
            heights = i
    print(cnt)


solution(arr)