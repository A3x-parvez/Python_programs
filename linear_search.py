arr=[1,2,3,5,6,9,100,200]

target = int(input("Enter the number : "))

for i in range(len(arr)):
    if arr[i]==target:
        print(f"Number at position {i+1}")

   