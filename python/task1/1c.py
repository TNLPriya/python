import math
def distance(x1, y1, z1, x2, y2, z2):
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    print("Distance is", d)
x1 = float(input("Enter the X1-coordinate: "))
y1 = float(input("Enter the Y1-coordinate: "))
z1 = float(input("Enter the Z1-coordinate: "))
x2 = float(input("Enter the X2-coordinate: "))
y2 = float(input("Enter the Y2-coordinate: "))
z2 = float(input("Enter the Z2-coordinate: "))
distance(x1, y1, z1, x2, y2, z2)
