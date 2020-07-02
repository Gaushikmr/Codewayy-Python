Question:1

def speedCheck(speed):
    speedLimit = 70
    if(speed <= speedLimit):
        print("OK")

    else:
        
        demeritPoint = 1

        for index in range(speedLimit + 5, speed):
            if(index %5 == 0):
                demeritPoint += 1
        print("Points:",demeritPoint)
        
        if(demeritPoint > 12):
            print("License suspended")



speed = int(input("Enter the speed of the driver:"))

speedCheck(speed)
