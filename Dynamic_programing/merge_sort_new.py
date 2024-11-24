inp = input("Enter the numbers (space-separated): ").split(",")
arr = [int(x) for x in inp]

print("Before sorting: ", arr)

def Merge_sort(array):
    # Base case: if array has 1 or no elements, it's already sorted
    if len(array) <= 1:
        return array
    #devide the array into small array untill the size of every array is 1
    mid = len(array) // 2
    left_arr = array[:mid]
    right_arr = array[mid:]

    # Recursively split and merge
    l_half = Merge_sort(left_arr)
    r_half = Merge_sort(right_arr)

    # Merge sorted halves
    return Merge(l_half, r_half)



def Merge(left_half,right_half):
    new = []
    i,j = 0,0
    while i<len(left_half) and j<len(right_half):
        if left_half[i] < right_half[j]:
            new.append(left_half[i])
            i=i+1
        else:
            new.append(right_half[j])
            j=j+1
            
    new.extend(left_half[i:])
    new.extend(right_half[j:])
    
    return new

new_arr = Merge_sort(arr)
print("After sorting : ",new_arr)
    