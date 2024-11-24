inp = input("Enter array eliments : ").split(",")
arr = [int(n) for n in inp]

num = int(input("Enter the number : "))

def binary_search(array,number,start,end):
    start = int(start)
    end = int(end)
    mid = (start+end)//2
    
    if start>end:
        print("invalid parameters")
        return    

    if array[mid] == number:
        print(f"The number present at {mid+1} position ")
    elif(array[mid] < number):
        binary_search(array,number,mid+1,end)
    elif(array[mid] > number):
        binary_search(array,number,start,mid-1)
    else:  
        print("The number doesnot exist into the list")


binary_search(array=arr,number=num,start=0,end=(len(arr)-1))
