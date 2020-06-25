# Question 1:

# Function to return Full Name
def conName(firstName,lastName):
    fullName = firstName+ " " + lastName
    return(fullName)

# Function to calculate total marks
def calculatetotalMarks(list_Subjects):
    totalMarks=sum(list_Subjects)
    return(totalMarks)

# Function to calculate Percentage
def calculatePercentage(number_Subject,totalMarks):
    Percentage = totalMarks/number_Subject
    return(Percentage)

# Function to calculate Grades
def calculateGrade (Marks):
     if(Marks >= 95):
        return('A')
     elif(Marks >= 85 and Marks <= 95):
        return('B')
     elif(Marks >= 75 and Marks <= 85):
        return('C')
     elif(Marks >= 65 and Marks <= 75):
        return('D')
     else:
        return("F")

# Function to display  the details
def displayDetails (firstName,lastName,number_Subject,list_Subjects):
    # conName function
    print("Full Name:", conName(firstName,lastName))
    
    # calculatetotalMarks Function
    totalMarks= calculatetotalMarks(list_Subjects)
    print("Total Marks:",totalMarks)
    
    # calculatePercentage function
    Marks=calculatePercentage(number_Subject,totalMarks)
    print("Marks in Percentage:",Marks)
    
    # calculateGrade function
    Grade=calculateGrade(Marks)
    print("Grade: ", Grade)
    
    
# Taking first and lastname as inputs      
firstName = input("Enter your Name: ")
lastName = input ("Enter your Surname:")

#Declaring an empty list
list_Subjects=[]

#Taking input of number of subjects
number_Subject=int(input("Enter number of subjects:"))

#Adding marks to the list
for n in range(number_Subject):
    marks=int(input("enter marks : "))
    list_Subjects.append(marks)

# DisplayDetails function
displayDetails (firstName,lastName,number_Subject,list_Subjects)
