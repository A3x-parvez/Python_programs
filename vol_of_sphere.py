radious = float(input("Enter the radious :"))
pi = 3.14

def volume(r):
    v=(4/3)*pi*r*r*r
    print(f"The volume of the sphere is = {v}")

volume(radious)