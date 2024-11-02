p = float(input("Enter the principle amount : "))
r = float(input("Enter the rate of interest : "))
t = float(input("Enter the time : "))

def simple_interest():
    interest = p*(1+(r/100))**t
    return interest

val =simple_interest()
print(f"The complex interest of Rs:{p} for {t} years with {r}% interest is = {val}")