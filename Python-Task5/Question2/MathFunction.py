**Question:2**

#Import math Library
import math

#returns the squareroot of number
num=int(input("Enter a number:"))
print(math.sqrt(num))

#return the ceil value
Num=float(input("Enter a float number:"))
print(math.ceil(Num))

#return the floor value
print(math.floor(Num))


#sorting the list
print("\nSorted List:")
Sort_List=[2,4,6,7,8]
print("Original List:",Sort_List)
Sort_List.sort()
print("List after sorting:",Sort_List)

#sorting the tuples
print("\nSorting of Tuples:")
Sort_Tuple=(5,7,2,3,4,)
print("Original Tuple list:",Sort_Tuple)
new_tuple=sorted(Sort_Tuple)
print("Sorted tuple:",new_tuple)


#sorting of set
print("\nSorting of Set:")
sortColors = {'red', 'green', 'yellow', 'blue', 'pink'}
print("Original set:",sortColors)
print("Sorted List from Set = ", sorted(sortColors))

