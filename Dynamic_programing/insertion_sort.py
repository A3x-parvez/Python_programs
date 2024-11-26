inp = input("Enter the eliments : ").split(" ")
arr = [int(x) for x in inp ]

print("Unsorted array : ",[i for i in arr])

def insertion_sort(arr):
    lenth = len(arr)

    for i in range(1,lenth):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1]=key


insertion_sort(arr)
print("sorted array : ",[i for i in arr])