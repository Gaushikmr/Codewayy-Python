# QUestion:7

def check_marks():
    
    mark = int(input("Enter marks:"))
    
    
    try:
        if(mark <90):
            raise Exception
                
    except Exception:
        print("Not Eligible!!!")
    else:
        print("Eligible.Congrats!!")    
  
    

check_marks()
