# Selection Sort 
# 1- select the smallest element in the collection,swap with the first element
# 2- Repeat the process with the 2nd smallest, 3rd smallest, etc.
# You will need to pass
# TO-DO: Complete the selection_sort() function below 

def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr)-1):
        min_index = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for n in range(i+1, len(arr)):
            if arr[n] < arr[min_index]:
                min_index = n
      
        # TO-DO: swap
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

print(selection_sort([5, 1, 3, 2, 4]))


# TO-DO:  implement the Bubble Sort function below
# Start at beginning and compare each element to its right hand neighbor. 
# If the right hand neighbor is smaller, we swap the two neighbors.
# The above process is repeated until we pass through the entire collection without performing a single swap. 
# With each pass, the larger elements will “bubble” toward the right hand side of the collection.
def bubble_sort( arr ):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print(bubble_sort([3, 2, 1, 7, 4]))


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr