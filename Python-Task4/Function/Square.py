#Function to calculate the square of number


def square_number ( number ) :
    square_Number = number**2
    print("Square Number is :",square_Number)

#Function to find maximum number in the list
def findMax(List) :
    max = 0
    for i in List :
        if ( max < i ) :
            max = i
    print("Maximum number in the list : ",max)

#Function to find minimum number in the list
def findMin(List):
    min = List[0]
    for i in List:
        if ( min > i ) :
            min = i
    print("Minimum number in the list : ", min)

# Function to find sum of numbers in the list
def sum(List):
   sum = 0
   for number in List:
        sum = sum + number
   print("Sum Of all numbers in the list :",sum)
