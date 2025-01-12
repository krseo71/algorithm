# 이차원 정수 배열 arr이 매개변수로 주어집니다. arr의 행의 수가 더 많다면 열의 수가 행의 수와 같아지도록
# 각 행의 끝에 0을 추가하고, 열의 수가 더 많다면 행의 수가 열의 수와 같아지도록
# 각 열의 끝에 0을 추가한 이차원 배열을 return 하는 solution 함수를 작성해 주세요.

def solution(arr):
    answer = []
    row = len(arr)
    col = len(arr[0])
    if row > col:
        for i in arr:
            answer.append(i + [0]*(row-col))
    elif row < col:
        for i in range(col - row):
            arr.append([0] * col)
        answer = arr
    else:
        answer = arr

    return answer
    print(f'row={row}, col={col}')



solution([[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]])