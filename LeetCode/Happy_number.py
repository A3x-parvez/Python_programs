def HappyNumber(n):
    if n <= 0:
        return False
    else:
        return cal(n,set())
    
def cal(n,seen):
    if n == 1:
        return True
    elif n in seen:
        return False
    else:
       seen.add(n)
       val = 0
       num_st = str(n)
       for i in num_st:
           val = val+ int(i)*int(i)
           
       return cal(val,seen)
    
print(HappyNumber(19))