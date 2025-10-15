list = [10, 20]
a = 30
list.append(a)
print(list)

list.pop(1)
print(list)
list.remove(10)
print(list)

l = [5, 8, 9, 15, 30, 89]
print(sorted(l))
print("The minimum value is:", min(l))
print("The maximum value is:", max(l))
print("The sum is:", sum(l))
print("The average is:", (sum(l) / len(l)))
