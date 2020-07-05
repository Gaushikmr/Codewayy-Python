class Student:
    
    def __init__(self, first, last, Marks):
        self.first = first
        self.last = last
        self.Marks = Marks
    
    # Method to return fullname
    def fullname(self):
        return "{} {}".format(self.first, self.last)
    
    # method to calculate total marks
    def calculateMarks(self):
        totalMarks = sum(self.Marks)
        return totalMarks
    
    # Method to calculate percentage
    def calculatePercentage(self, totalMarks):
        percentage = totalMarks / len(self.Marks)
        return percentage

    # Function to calculate Grade
    def calculateGrade(self, Percentage):
        if Percentage >= 95:
            return 'A'
        elif 85 <= Percentage <= 95:
            return 'B'
        elif 75 <= Percentage <= 85:
            return 'C'
        elif 65 <= Percentage <= 75:
            return 'D'
        else:
            return "F"

    # function to display all the details
    def displayDetails(self):
       
        print("Name: ", self.fullname())

        
        totalMarks = self.calculateMarks()
        print("Total Marks:", totalMarks)

        
        Percentage = self.calculatePercentage(totalMarks)
        print("Score in Percentage:", Percentage)

       
        Grade = self.calculateGrade(Percentage)
        print("Grade: ", Grade)


# providing data 
stud_1 = Student("sibin", "m", [80, 98, 97, 82])
stud_2 = Student("sidhin", "m", [50, 60, 70, 80])


# Displaying detail of student 1
print("\nDetails of Student1:")
stud_1.displayDetails()

# Displaying detail of student 2
print("\nDetails of Student2:")
stud_2.displayDetails()


