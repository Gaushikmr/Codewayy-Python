#Question2

#Taking information from user

#Input name
firstname = input("Enter First Name: ")
lastname = input("Enter Last Name: ")

#Input college
collegename = input("Enter College Name: ")
collegeaddress = input("Enter College Address: ")

#inputs for marks of five subjects
mark1 = float( input("Enter marks of Subject 1: "))
mark2 = float( input("Enter marks of Subject 2: "))
mark3 = float( input("Enter marks of Subject 3: ")) 
mark4 = float( input("Enter marks of Subject 4: "))
mark5 = float( input("Enter marks of Subject 5: "))

#String concatenation for full name
fullname = firstname + " " + lastname

#String concatenation for college
college = collegename + ", " + collegeaddress

#Calculating total marks and percentage
total_marks = mark1 + mark2 + mark3 + mark4 + mark5
percentage = ( total_marks / 5)

#Displaying the information
print("Name: ",fullname)
print("College: ",college)
print("Total marks obtained: ",total_marks)
print("Percentage: ",percentage)
