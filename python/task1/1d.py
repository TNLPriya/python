import math
def equationroots(x, y, z):
    discri = y * y - 4 * x * z
    sqrtval = math.sqrt(abs(discri))
    if discri > 0:
        print("Roots are real and different")
        print((-y + sqrtval) / (2 * x))
        print((-y - sqrtval) / (2 * x))
    elif discri == 0:
        print("Roots are real and same")
        print(-y / (2 * x))
    else:
        print("Roots are complex")
        print(-y / (2 * x), "+ i", sqrtval)
        print(-y / (2 * x), "- i", sqrtval)
x = int(input("Enter a: "))
y = int(input("Enter b: "))
z = int(input("Enter c: "))
if x == 0:
    print("Input correct quadratic equation")
else:
    equationroots(x, y, z)
