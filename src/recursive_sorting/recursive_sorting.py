# TO-DO: complete the helper function below to merge 2 sorted arrays *
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    print("Merged Arr", merged_arr)
    print("Arrays A and B:", arrA, arrB)
    # TO-DO
    # 3. Merging single lists into larger, sorted sets
    # Repeat 3 until entire set has been merged
    # Counters to store indexes
    indexA = 0
    indexB = 0

    # Stepping through merged array with placeholders
    for i in range(elements):
        if indexA >= len(arrA):
            # a empty, b not empty
            merged_arr[i] = arrB[indexB]
            indexB += 1
        elif indexB >= len(arrB):
            # B is empty, A is not empty
            merged_arr[i] = arrA[indexA]
            indexA += 1
        elif arrA[indexA] < arrB[indexB]:
            # A has smaller num
            merged_arr[i] = arrA[indexA]
            indexA += 1
        else:
            # B has smaller num
            merged_arr[i] = arrB[indexB]
            indexB += 1

    print(merged_arr)
    return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    # Split if array length > 1
    print(f"MERGE SORT: {arr}")

    if len(arr) > 1:
        # Split array into two halves; rounding down
        mid = len(arr) // 2
        leftArr = arr[:mid]  # split the original arr into a left
        rightArr = arr[mid:]  # middle to rest of array

        # Sort each of the split arrays - split further using recursion
        sortLeft = merge_sort(leftArr)  # Will repeat into arr > 1
        # Will repeat into arr > 1 but after sortLeft
        sortRight = merge_sort(rightArr)

        # Merge the sorted arrays using the helper function
        arr = merge(sortLeft, sortRight)

    return arr


merge_sort([2, 1, 5, 6, 0])


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
