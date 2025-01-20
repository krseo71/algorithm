# 한 개의 문장이 주어지면 그 문장 속에서 가장 긴 단어를 출력하는 프로그램을 작성하세요.
# 문장속의 각 단어는 공백으로 구분됩니다.

def largest(str):
    arr = str.split()
    sorted_arr = sorted(arr, key=len, reverse=True)
    print(sorted_arr[0])

largest(input())