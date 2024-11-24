def Merge_Array(arr1,m,arr2,n):
    n_arr1 = []
    n_arr2 = []
    
    for i in range(m):
        n_arr1.append(arr1[i])
        
    for i in range(n):
        n_arr2.append(arr2[i]) 
        
    new_arr = sorted(n_arr1+n_arr2)
    arr1 = new_arr
    return arr1

print(Merge_Array([1,2,3,0,0,0],3,[2,5,6],3))   
print(Merge_Array([1],1,[],0))   
print(Merge_Array([0],0,[1],1))   
    