tuple1 = (10, 'hello', 3.14, 'world')
print(tuple1)

for i in tuple1:
    print(i)

print(tuple1[1:3])
print(tuple1[:-1])

t2 = (5, 0.5)
t3 = tuple1 + t2
print(t3)

try:
    tuple1[3] = "PI"
except TypeError as e:
    print("Error:", e)
