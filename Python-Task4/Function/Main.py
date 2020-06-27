#importing modules of square string and logical operators
import logical
import  square
import string

#calling all the functions of Square module
print("------functions of list-------")
List = [2,4,7,8,9]
square.square_number(10)
square.findMax(List)
square.findMin(List)
square.sum(List)
print()

#calling all the functions of Strings module
print("-------functions of string-------")

String = input("Enter the string :")
string.find_middle_character(String)
string.length_of_string(String)
string.Vowel_in_string(String)

#calling all the functions of LogicalOperators module
print("-------functions of logical operators-------")
x = int(input("enter the first number: "))
y = int(input("enter the second number: "))
logical.andOperator(x, y)
logical.orOperator(x, y)
logical.notOperator(x, y)
