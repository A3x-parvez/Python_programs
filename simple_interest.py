p = float(input("Enter the principle amount : "))
r = float(input("Enter the rate of interest : "))
t = float(input("Enter the time : "))

def simple_interest():
    interest = (p*t*r)/100
    return interest

val = simple_interest()
print(f"The simple interest of Rs:{p} for {t} years with {r}% interest is = {val}")
print(f"The total amount you need to pay is = {p+val}")