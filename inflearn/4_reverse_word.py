# N개의 단어가 주어지면 각 단어를 뒤집어 출력하는 프로그램을 작성하세요.

n = int(input())
def reverseWord(str):
    return str[::-1]
for _ in range(n):
    print(reverseWord(input()))

