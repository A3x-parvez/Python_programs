inp = input("Enter the number : ").split(" ")
arr = [int(x) for x in inp]

print("Unsorted array : ",[i for i in arr])

def bubble_sort(array):
    n = len(array)
    
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                
bubble_sort(array=arr)

print("Sorted array",[i for i in arr])