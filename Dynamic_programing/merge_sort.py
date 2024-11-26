import numpy as np

inp = input("Enter the numbers (space-separated): ").split(" ")
arr = [int(x) for x in inp]

print("Before sorting: ", arr)

def Merge(array, lower_bound, upper_bound):
    mid = (lower_bound + upper_bound) // 2
    i = lower_bound
    j = mid + 1
    k = 0
    new_arr = np.zeros(len(array), dtype=int)
    
    # Merging two halves
    while i <= mid and j <= upper_bound:
        if array[i] < array[j]:
            new_arr[k] = array[i]
            i += 1
        else:
            new_arr[k] = array[j]
            j += 1
        k += 1
    
    # Copy remaining elements from left half
    while i <= mid:
        new_arr[k] = array[i]
        i += 1
        k += 1
    
    # Copy remaining elements from right half
    while j <= upper_bound:
        new_arr[k] = array[j]
        j += 1
        k += 1
    
    # Copy back to original array
    for idx in range(lower_bound, upper_bound + 1):
        array[idx] = new_arr[idx - lower_bound]


def Merge_sort(array, lower_bound, upper_bound):
    if lower_bound < upper_bound:
        mid = (lower_bound + upper_bound) // 2
        # Recursively split and merge
        Merge_sort(array, lower_bound, mid)
        Merge_sort(array, mid + 1, upper_bound)
        # Merge sorted halves
        Merge(array, lower_bound, upper_bound)


Merge_sort(arr, 0, len(arr) - 1)
print("After sorting: ", arr)
