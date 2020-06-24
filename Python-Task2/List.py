# Method of lists in python:

# Lst declaration
list = [12, 45, 70, 88, 42, 99]

# printing the list
print('list:', list)

# Adding  the elements to  last position of List.
list.append(58)
print('appended list:', list)

# Printing the index of element
print('58 is at index:', list.index(58))
List2 = [89, 37]

# Adding contents of List2 to the end of list
list.extend(List2)
print('After extending the  list:', list)

# Inserting an elements at specified position
list.insert(4, 67)
print("67 is inserted at 2nd position:", list)

# Calculating sum of all the elements of List
print('sum of all elements', sum(list))

# Removing the last element of the list
print('Removed element:', list.pop())

# Printing minimum element in the list
print('Minimum element in list:', min(list))

# Printing maximum element in the list
print('Maximum element in list:', max(list))
