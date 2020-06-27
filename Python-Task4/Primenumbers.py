#Question:1

# Initializing matrix 

matrix = [] 

# Taking input from user of rows and column

row = int(input("Enter the number of rows:")) 
column = int(input("Enter the number of columns:"))
print("Enter the elements row wise:")

# Getting elements of matrix from user

for i in range(row):         
    a =[]
    
    for j in range (column):      
         a.append(int(input())) 
    matrix.append(a) 
print()
  
# Printing user entered  matrix
print("Entered Matrix is: ")
for i in range(row): 
    for j in range(column): 
        print(matrix[i][j], end = " ") 
    print()
print()

#Printing prime numbers of matrix:

print("The prime numbers in  the matrix are: ")
for i in range(row): 
    for j in range(column): 

        if( matrix[i][j] > 1):

         
            for p in range(2, matrix[i][j]):

              
                if(matrix[i][j] % p) == 0:
                    break
            else:
            
                print(matrix[i][j])



