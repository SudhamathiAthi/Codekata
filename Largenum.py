num1=input("Enter the First number:")
    num2=input("Enter the Second number:")
    num3=input("Enter the Third number:")
    if(num1>num2 and num1>num3):
        print "The largest number is "+str(num1)
    elif(num2>num1 and num2>num3):
        print "The largest number is "+str(num2)
    else:
        print "The largest number is "+str(num3)
