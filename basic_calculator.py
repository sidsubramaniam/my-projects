#Program to simulate a basic calculator

print("*** SIMPLE CALCULATOR ***")
print("this calculator can perform basic arithmetic operations (+,-,*,/)")
a=float(input("Enter number = "))
print(a)
op=str(input("Enter operator: "))
print(str(a) + op)
b=float(input("Enter number = "))
print(str(a) + op + str(b))
ev=str(input("to evaluate enter '=': "))
if ev=="=":
    if op=="+":
        print(str(a)+op+str(b)+"="+str(a+b))
        print("Thank you!")
    elif op=="-":
        print(str(a)+op+str(b)+"="+str(a-b))
        print("Thank you!")
    elif op=="*":
        print(str(a)+op+str(b)+"="+str(a*b))
        print("Thank you!")
    elif op=="/":
        print(str(a)+op+str(b)+"="+str(a//b))
        print("Thank you!")
    else:
        print("invalid entry, please try again :(")
        
else:
    print("invalid entry, please try again :(")




    



         
         

