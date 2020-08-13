# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    # * COUNTERS
    left = 0
    right = 0
    total = 0

    # * APPEND INDEXES TO MERGED ARRAY
    while left < len(arrA) and right < len(arrB):
        if arrA[left] < arrB[right]:
            merged_arr[total] = arrA[left]
            left += 1
        else:
            merged_arr[total] = arrB[right]
            right += 1
        total += 1

    # ? IS ARRAY A AND B EMPTY?
    while left < len(arrA):
        merged_arr[total] = arrA[left]
        left += 1
        total += 1

    while right < len(arrB):
        merged_arr[total] = arrB[right]
        right += 1
        total += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # Your code here
    if (len(arr) > 1):

        # * LEFT SIDE ARR
        left = merge_sort(arr[:len(arr) // 2])

        # * RIGHT SIDE ARR
        right = merge_sort(arr[len(arr) // 2:])

        arr = merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
    # Your code here


# def merge_sort_in_place(arr, l, r):
    # Your code here

