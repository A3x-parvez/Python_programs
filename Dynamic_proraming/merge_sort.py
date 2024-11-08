# import numpy as np
# inp = input("Enter the number :").split(" ")
# arr = [int(x) for x in inp]

# print("Before sorting : ",[i for i in arr])

# def Merge(array,lower_bound,upper_bound):
#     i=lower_bound
#     j=upper_bound
#     mid =(i+j)//2
#     k=mid+1
#     l=0
#     new_arr=np.zeros(dtype=int,shape=len(arr))
    
#     while (i<=mid and k<=j):
#         if(array[i]<array[j]):
#             new_arr[l] = array[i]
#             l=l+1
#             i=i+1
#         else:
#             new_arr[l] = array[k]
#             l=l+1
#             k=k+1
    
#     if(i>mid):
#         while (k<=j):
#             new_arr[l] = array[k]
#             l=l+1
#             k=k+1
        
#     if(k>j):
#         while(i<=mid):
#             new_arr[l]=array[i]
#             i=i+1
#             l=l+1
            
#     return list(new_arr)


# def Merge_sort(array,lowre_bound,upper_bound):
#     if l<u:
#         l= lowre_bound
#         u = upper_bound
#         mid = (l+u)//2
#         #split the array 
#         Merge_sort(array=array,lowre_bound=l,upper_bound=mid)
#         Merge_sort(array=array,lowre_bound=mid+1,upper_bound=u)
#         #add the array in sorted order
#         sorted = Merge(array=array,lowre_bound=l,upper_bound=u)
        
# s=Merge_sort(array=arr,lowre_bound=0,upper_bound=len(arr)-1)
# print("After sorting : ",s)


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
