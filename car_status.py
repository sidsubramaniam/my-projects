print("***CAR STATUS***")
print("Enter 'help' to display options.")
a=''
while(a!="help"):
    a=str(input(""))

    if a=="help":
        print("enter 'start' - to start the car")
        print("enter 'stop' - to stop the car")
        print("enter 'quit' - to exit program")
        while a=="help":
            b=str(input(""))
            if b=="start":
                print("Starting the car...")
            elif b=="stop":
                print("Stopping the car...")
            elif b=="quit":
                print("Thank you!")
                break
            else:
                print("Invalid entry")
    else:
        print("Invalid entry")
    

    

            

    
    



    


 
    

    
