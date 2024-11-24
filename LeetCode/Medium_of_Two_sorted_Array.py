def Median(n1,n2):
    n3 =sorted(n1+n2)
    l_n3 = len(n3)
    mid = 0.0
    
    if l_n3 % 2 == 0:
        m1 = l_n3//2
        m2 = m1+1
        mid = (n3[m1-1]+n3[m2-1])/2
    else:
        m = l_n3//2 +1
        mid = n3[m-1]
    return mid

print(Median([1,2],[3]))
print(Median([1,2],[3,4]))
print(Median([1,2,4,5],[3,4,8,10]))