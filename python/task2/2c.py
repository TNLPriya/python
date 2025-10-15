x = input()
c = 0
for i in x:
    if ord(i) >= 65 and ord(i) <= 90:
        c += 1
print(c + 1)
