# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
# base case
    # target was not found
    if start > end:
        return -1

    middle = (start + end) // 2
    
    # target was found at index 'middle'
    if target == arr[middle]:
        return middle
    
# move toward base case / make recursive call
    if target < arr[middle]:
        # target is in first half of list, so eliminate
        # second half of list and search again
        return binary_search(arr, target, start, middle - 1)
    else:
        # target is in second half of list, so eliminate
        # first half of list and search again
        return binary_search(arr, target, middle + 1, end)

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    start = 0
    end = len(arr) - 1
    isAscending = arr[start] < arr[end]
    
    while start <= end:
        mid = start + (end - start) // 2
        
        if target == arr[mid]:
            return mid
        
        if isAscending:
            if target < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if target > arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
    
    return -1