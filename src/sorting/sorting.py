# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    for i in range(elements):
        if not arrA:
            merged_arr[i] = arrB.pop(0)
        elif not arrB:
            merged_arr[i] = arrA.pop(0)
        elif arrA[0] < arrB[0]:
            merged_arr[i] = arrA.pop(0)
        else:
            merged_arr[i] = arrB.pop(0)
            
    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # base case
    if len(arr) <= 1:
        return arr

    # move toward base case
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]

    return merge(merge_sort(left), merge_sort(right))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    start2 = mid + 1
    
    # arr is already sorted
    if arr[mid] <= arr[start2]:
        return
    
    while start <= mid and start2 <= end:
        # check first element
        if arr[start] <= arr[start2]:
            start += 1
        else:
            value = arr[start2]
            i = start2
            
            # shift elements to right by 1
            while i != start:
                arr[i] = arr[i - 1]
                i -= 1
            
            arr[start] = value
            
            # update pointers
            start += 1
            mid += 1
            start2 += 1

def merge_sort_in_place(arr, l, r):
    # Your code here
    if l < r:
        
        # avoid overflow
        m = l + (r - l) // 2
        
        #sort first and second halves
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)
        
        merge_in_place(arr, l, m, r)
