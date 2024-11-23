def CountingBits(n):
    bit_count=[]
    
    for i in range(0,n+1):
        b_num = bin(i)[2:]
        c_bit = b_num.count("1")
        bit_count.append(c_bit)
        
    return bit_count

print(CountingBits(5))