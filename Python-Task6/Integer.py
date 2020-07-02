# Declaring and defining the function
def findType(n):
    i = 1
    sum = 0
    for i in range(1,n):
        if (n % i == 0):
                sum = sum + i
                
    if sum > n:
        return -1
    elif sum == n:
        return 1
    else:
        return 0



# Question:6
number = int(input("Enter a number:"))


numberType = findType(number)

if numberType == -1 :
    print("Abundant Number")
elif numberType == 1 :
    print("Perfect Number")
else :
    print("Deficient Number")
