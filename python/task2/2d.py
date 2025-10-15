a = int(input())
p = 0
b = a
while b > 0:
    r = b % 10
    p = p * 10 + r
    b = b // 10
if p == a:
    print("Mirror")
else:
    print("No Mirror")
