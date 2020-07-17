
class Person:

    def __init__(self, fullName):
        self.fullName = fullName


    def getPerson(self):
        print(self.fullName)


class Student(Person):

    def __init__(self, student_Id, fullName, coursesEnrolled, feePaid, list_courses, courseGrade):
        self.student_Id = student_Id
        Person.__init__(self, fullName)
        self.coursesEnrolled = coursesEnrolled
        self.feePaid = feePaid
        self.list_courses = list_courses
        self. courseGrade =  courseGrade


    def calFee(self):
        sum = 0


        for i in range(self.coursesEnrolled):
            sum += Course.crsCredit(self.list_courses[i])
        return (sum * 500)


    def calGPA(self):
        sum = 0
        x = 0
        gList = []

        # iterating to calculate the total credits of the courses enrolled by a student
        for i in range(self.coursesEnrolled):
            sum += Course.crsCredit(self.list_courses[i])

        # iterating to add grade values of the grades obtained by the students in enrolled courses
        for i in range(self.coursesEnrolled):
            if self. courseGrade[i] == "A":
                gValue = 4
            elif self. courseGrade[i] == "B":
                gValue = 3
            elif self. courseGrade[i] == "C":
                gValue = 2
            elif self. courseGrade[i] == "D":
                gValue = 1
            else:
                gValue = 0
            gList.append(gValue)

        # iterating to calculate x =   grade_values * course_credits
        for i in range(self.coursesEnrolled):
            x += Course.crsCredit(self.list_courses[i]) * gList[i]

        # gpa = (grade_values * course_credits) / total_credits
        gpa = x / sum
        return (gpa)

    # function to check if tution fee is paid or not
    def pFee(self):
        if (self.feePaid == 1):
            return 1
        else:
            return 0

    # function to display student id and name
    def dispStudent(self):
        print(self.student_Id, end="    ")
        Person.getPerson(self)

    # fiunction to display the list of students and courses enrolled by them along with tution fee and gpa
    def stuEnrollment(self, flag):
        print(self.student_Id, end="")
        Person.getPerson(self)
        print("Course ID       Course Name    Course Credit Grades")
        for i in range(self.coursesEnrolled):
            Course.getCourse(self.list_courses[i])
            print(self. courseGrade[i])

        tutionFee = Student.calFee(self)
        if (flag == 0):
            print("Tution Fee:", tutionFee, "baht")
        else:
            print("Tution Fee paid:", tutionFee, "baht")
        gpa = Student.calGPA(self)
        print("GPA:", gpa)


# class Course
class Course:
    # constructor for class Course
    def __init__(self, course_Id, c0urse_Name, course_Credits):
        self.course_Id = course_Id
        self.c0urse_Name = c0urse_Name
        self.course_Credits = course_Credits

    # function to print course details
    def getCourse(self):
        print(self.course_Id, end="    ")
        print(self.c0urse_Name, end="    ")
        print(self.course_Credits, end="   ")

    # function to return credits
    def crsCredit(self):
        return (self.course_Credits)


# function to display menu
def menu():
    print("***MENU***")
    print("1.List Courses")
    print("2.List Students")
    print("3.List Students and Enrollment")
    print("4.Grade Report")
    print("-1.Exit")


# function to create and add objects of class Course to the cList
def courseList(cList):
    # creating object
    objCrs1 = Course(1234, "Object-Oriented in C++", 3)
    # adding the object to the list
    cList.append(objCrs1)

    objCrs2 = Course(1235, "Financial Engineering", 3)
    cList.append(objCrs2)
    objCrs3 = Course(1236, "Discrete Mathamatics", 3)
    cList.append(objCrs3)
    objCrs4 = Course(1237, "Intro Social Science", 2)
    cList.append(objCrs4)
    objCrs5 = Course(1238, "Intro Linear Algebra", 3)
    cList.append(objCrs5)
    objCrs6 = Course(1239, "Fundamental English", 2)
    cList.append(objCrs6)
    objCrs7 = Course(1240, "Fundamental Japanese", 2)
    cList.append(objCrs7)


# function to create and add objects of class Student to the sList
def studentList(sList, cList):
    objStu1 = Student(12345, "John Wayn", 4, 1, [cList[0], cList[1], cList[5], cList[6]], ['A', 'B', 'B', 'A'])
    sList.append(objStu1)
    objStu2 = Student(12346, "Jane March", 5, 1, [cList[1], cList[2], cList[4], cList[5], cList[6]],
                      ['A', 'B', 'B', 'C', 'D'])
    sList.append(objStu2)
    objStu3 = Student(12347, "Marry Dolphin", 5, 0, [cList[0], cList[3], cList[4], cList[5], cList[6]],
                      ['C', 'B', 'C', 'A', 'B'])
    sList.append(objStu3)


def main():
    # declaring an empty list to add objects of class Course
    cList = []
    courseList(cList)

    # declaring an empty list to add objects of class Student
    sList = []
    studentList(sList, cList)

    choice = 0

    while choice >= 0:
        # calling of menu()
        menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Course ID       Course Name        Course Credit")

            # iterating to print the list of available courses
            for i in range(cList.__len__()):
                Course.getCourse(cList[i])
                print()
            print()

        if choice == 2:
            print("Student ID       Student Name")

            # iterating to print the list of students
            for i in range(sList.__len__()):
                Student.dispStudent(sList[i])
            print()

        if choice == 3:

            # iterating to print the list of students and their enrollement
            for i in range(sList.__len__()):
                Student.stuEnrollment(sList[i], 0)
            print()

        if choice == 4:
            for i in range(sList.__len__()):
                if sList[i].pFee() == 1:
                    # if fee is paid
                    Student.stuEnrollment(sList[i], 1)
                else:
                    # if fee is not paid
                    Student.dispStudent(sList[i])
                    print("You need to pay the tution fee of", Student.calFee(sList[i]), "baht")
            print()

        if choice == -1:
            print("Ending!!!")


# calling the main function
main()
