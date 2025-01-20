import sys

def solution(s):
    arr = s.split()
    for i in range(len(arr)):
        if len(arr[i]) > 1: # 단어의 길이가 1보다 큰경우
            arr[i] = arr[i][::-1] # 슬라이싱을 이용해 단어를 뒤집음

    print(' '.join(arr)) # 뒤집힌 단어들을 공백으로 연결해 출력

N = int(sys.stdin.readline())
for _ in range(N):
    solution(sys.stdin.readline())