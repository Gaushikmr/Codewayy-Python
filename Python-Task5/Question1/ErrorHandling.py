**Question:1**

try:
    

    num1 = int(input("Enter any number:"))
    num2 = int(input("enter any number:"))
    
    k = num1 + num2
    print(k)
    
  
    raise ValueError("Error:Result is zero")
# exception ValueError:
except ValueError as j:
    print(j)
finally:
    print("Sucess")
