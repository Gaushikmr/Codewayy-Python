# Question:3

string = input("Enter any string:").split()


list1=[]


for i in string:
    for j in i:
        list1.append(j)
        

lower=upper=0
for j in list1:
    
   
    if(j.islower()):
        lower=lower+1
        
    
    elif(j.isupper()):
        upper=upper+1
        
print("Upper:",upper)
print("Lower", lower)
