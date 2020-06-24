#Dictionary Methods i Python:

# Declaration of dictionaries
dict = {'Name': 'John', 'Age': 25, 'Course': 'Computer Science'}

# Accessing elements using keys
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])

# Adding new entry
dict['College'] = " Amrita "
print('dict:', dict)

# Removeing the  entry with key 'Name'
del dict['Name']
print('dict:', dict)

# Returning a list of dict's (key, value) tuple pairs
print('dict:', dict.items())

# printing the length of dictionary
print('length of dictionary: ', len(dict))

#Removing  the inserted key-value pair
print("recently added item removed:", dict.popitem())

# Sorting key values in alphabetical order
print("sorted dictionary:", sorted(dict))

# Printing list of keys
print("List:", list(dict))
