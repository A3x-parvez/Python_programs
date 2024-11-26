def romanToInt(s):
    # Roman numeral values
    roman_map = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    
   # Check if all characters in the string are valid Roman numerals
    for char in s:
        if char not in roman_map:
            return "Enter a valid string"
    
    for i in range(len(s)):
        # Get the value of the current Roman numeral
        current_value = roman_map[s[i]]
        
        # If this is not the last character and the next character represents a larger value, subtract the current value
        if i+1 < len(s) and current_value < roman_map[s[i+1]]:
            total = total-current_value
        else:
            total = total+current_value
            
    return total
        
# Test cases
print(romanToInt("III"))        # Output: 3
print(romanToInt("LVIII"))      # Output: 58
print(romanToInt("MCMXCIV"))    # Output: 1994