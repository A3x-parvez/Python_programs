inp = input("Enter the numbers :").split(" ")
arr = [int(val) for val in inp]

print("Before sorting : ",[i for i in arr])

def selection_sort(array):
    n=len(arr)
    
    for i in range(0,n-1):
        for j in range(i+1,n):
            if array[i]>array[j]:
                array[i],array[j] = array[j] , array[i]
                
selection_sort(array=arr)
print("After sorting : ",[i for i in arr])