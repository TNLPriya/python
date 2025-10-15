dictionary = {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(dictionary)

print(dictionary['name'])
print(dictionary['age'])

dictionary['name'] = "James"
print(dictionary)
dictionary.pop('city')
print(dictionary)

for k in dictionary:
    print("KEY:", k)

print(dictionary.items())
