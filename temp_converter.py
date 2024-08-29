print("    ## Welcome to the tempreature converter ##")
print("--------------------------------------------------")
while True:
    temp = input("Enter the tempreature (eg:100C or 100F / X for Exit) : ")
    temp=temp.lower()
    temp_n=temp.replace(".","")
    
    if temp_n.startswith("-"):
        temp_n=temp_n.replace("-","",1)
        
    l=len(temp_n)
    conv_temp=0
    
    
    if (temp_n[0:l-1].isdigit() and (temp_n.endswith("f") or temp_n.endswith("c")) and temp.count(".")<=1):
        print("Tempreature Convert Sucessfully.")
        if "c" in temp:
            temp_val = float(temp.replace("c",""))
            conv_temp = ((9/5)*temp_val)+32
            print(f"Ans : {temp_val}C in Fahrenheit is {conv_temp}F .\n")
            
        elif "f" in temp:
            temp_val = float(temp.replace("f",""))
            conv_temp = (temp_val-32)*(5/9)
            print(f"Ans : {temp_val}F in Celcious is {conv_temp}C .\n")
            
    elif "x" in temp:
        print("Sucessfully Exit.")
        break
    
    else:
        print("Enter valid input and follow the format.\n")



    