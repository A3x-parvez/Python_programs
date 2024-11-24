def split_with_minimum_sum(num: int) -> int:
    # Convert the number to a sorted list of digits
    digits = sorted(str(num))
    
    # Distribute the digits alternately between num1 and num2
    num1, num2 = [], []
    for i, digit in enumerate(digits):
        if i % 2 == 0:
            num1.append(digit)
        else:
            num2.append(digit)
    
    # Convert the digit lists back into integers
    num1 = int(''.join(num1))
    num2 = int(''.join(num2))
    
    # Return the minimum sum
    return num1 + num2

# Examples
print(split_with_minimum_sum(4325))  # Output: 59
print(split_with_minimum_sum(687))   # Output: 75
