user=input("Enter the list of transaction : ").split(",")
s=[x for x in user]
bal=0
for i in s:
    if "D" in i :
        i=i.replace("D","")
        i=float(i)
        bal=bal+i
    elif "W" in i:  
         i=i.replace("W","")
         i=float(i) 
         bal=bal-i
    else:
        pass

print(f"Total balance is : {bal}")