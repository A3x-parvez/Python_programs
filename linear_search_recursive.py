arr =[1,2,3,4,5,6,12,13,1,4,45,67]

target = int(input("Enter the number : "))

index=0

def linear_search(arr,index,t):
    if arr[index]==t:
        return index+1
    elif arr[len(arr)-1]==t:
        return len(arr)
    else:
        linear_search(arr,index+1,t)
    
print(linear_search(arr,index,target))