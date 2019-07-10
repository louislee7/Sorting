# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    x = 0
    y = 0
    i = 0
    # sorting array
    while x < len(arrA) and y < len(arrB):
        if arrA[x] < arrB[y]:
            merged_arr[i] = arrA[x]
            x += 1
        else:
            merged_arr[i] = arrB[y]
            y += 1
        i += 1
    while x < len(arrA):
        merged_arr[i] = arrA[x]
        x += 1
        i += 1
    while y < len(arrB):
        merged_arr[i] = arrB[y]
        y += 1
        i += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if len(arr) > 1:
        middle = len(arr)/2
        arrL = arr[:int(middle)]
        arrR = arr[int(middle):]
        arrL = merge_sort(arrL)
        arrR = merge_sort(arrR)
        return merge(arrL, arrR)
    else:
        return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
