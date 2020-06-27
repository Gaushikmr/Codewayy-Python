#Function for and operator
def andOperator(x,y):
        if (x > 0 and y > 0 ):
            print("Both  are Positive numbers")

#Function for or operator
def orOperator(p,q):
   if(p > 0 and q > 0):
       print ("Atleast one is Positive number")    

#Function for not operator
def notOperator(x,y):
    if not(x % 2==0 or y %2 == 0):
        print("num is divisible by 2")
