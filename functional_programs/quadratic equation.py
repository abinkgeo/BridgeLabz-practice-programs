import math

a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))

delta = b*b - 4*a*c

if delta > 0:
    root1 = (-b + math.sqrt(delta)) / (2*a)
    root2 = (-b - math.sqrt(delta)) / (2*a)
    print("Two real roots:")
    print("Root 1:", root1)
    print("Root 2:", root2)

elif delta == 0:
    root = -b / (2*a)
    print("One real root:")
    print("Root:", root)

else:
    print("No real roots ")
