def sortPeople(name,height):
    
    pairs =list(zip(height,name))
    pairs.sort(reverse = True)
    return [name for _,name in pairs]
    
    
print(sortPeople(["Mary", "John", "Emma"], [180, 165, 170]))
print(sortPeople(["Rohit", "Jerry", "Emely", "Brian" ,"Steewe", "quagmire"], [150, 165, 170,100,110,170]))