array = [5, 3, 2, 1, 6, 8, 7, 4]

def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_array = array[:mid]
    right_array = array[mid:]
    print(array)
    print('left_array', left_array)
    print('right_array', right_array)
    return merge(merge_sort(left_array), merge_sort(right_array))

def merge(array1, array2):
    print('array1, array2 =', array1, array2)
    result = []
    array1_index = 0
    array2_index = 0

    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1
    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1
    print('result =', result)
    return result

print(merge_sort(array))


# merge_sort([5, 3, 2, 1, 6, 8, 7, 4])
#     ├── merge_sort([5, 3, 2, 1])
#     │      ├── merge_sort([5, 3])
#     │      │      ├── merge_sort([5]) → [5]
#     │      │      ├── merge_sort([3]) → [3]
#     │      │      └── merge([5], [3]) → [3, 5]
#     │      ├── merge_sort([2, 1])
#     │      │      ├── merge_sort([2]) → [2]
#     │      │      ├── merge_sort([1]) → [1]
#     │      │      └── merge([2], [1]) → [1, 2]
#     │      └── merge([3, 5], [1, 2]) → [1, 2, 3, 5]
#     ├── merge_sort([6, 8, 7, 4])
#     │      ├── ...
#     │      └── merge([6, 8], [4, 7]) → [4, 6, 7, 8]
#     └── merge([1, 2, 3, 5], [4, 6, 7, 8]) → [1, 2, 3, 4, 5, 6, 7, 8]
