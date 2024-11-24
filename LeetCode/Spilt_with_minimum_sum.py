def split_with_minimum_sum(num):
    digits = sorted(str(num))
    
    num1 ,num2 =[] ,[]
    for i,digt in enumerate(digits):
        
        if i%2 == 0:
            num1.append(digt)
        else:
            num2.append(digt)
            
    num1 = int("".join(num1))
    num2 = int("".join(num2))
    
    return num1+num2

# Examples
print(split_with_minimum_sum(4325))  # Output: 59
print(split_with_minimum_sum(687))   # Output: 75
