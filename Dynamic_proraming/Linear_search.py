user=input("Enter the list of numbers : ").split(",")
arr=[int(x) for x in user]

num = int(input("Enter the number you want to search : "))


def linearsearch(array,num):
    for i in range(len(array)):
        if array[i] == num:
            return i+1
    return "Eliment not found"   

index = linearsearch(array=arr,num=num)
print("The position is : ",index)