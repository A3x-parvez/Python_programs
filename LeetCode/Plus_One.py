def PlusOne(num):
    #create a empty string
    val=""
    #add every digit from list oneby one  
    for i in num:
        val = val+str(i)
    #convert the string with int and add 1
    value = int(val)+1
    #take a new empty list
    new_l=[]
    #convert the int into a string
    value_s = str(value)
    #iterate the string and add every eliment into a new list
    for i in value_s:
        new_l.append(int(i))
    #old list
    print(num)
    #add one new list   
    print(new_l)
    
PlusOne([1,2,3])
PlusOne([4,3,2,1])
PlusOne([9])