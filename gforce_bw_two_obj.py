m1 = float(input("Enter the mass of 1st object : "))
m2 = float(input("Enter the mass of 2nd object : "))
l = float(input("Enter the distance between the objects : "))
G = 6.67*10
def g_force():
    gf = (G*m1*m2)/l**2
    return gf

print(f"The Gravitational force between this two objects is : {g_force()}N .")