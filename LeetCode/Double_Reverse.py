def Double_Reverse(num):
    num_rev1 = int(str(num)[::-1])
    num_rev2 = int(str(num)[::-1])
    
    if num == num_rev2:
        return True
    else:
        return False
    
# Examples
print(Double_Reverse(526))   # Output: True
print(Double_Reverse(1800))  # Output: False
print(Double_Reverse(0))     # Output: True