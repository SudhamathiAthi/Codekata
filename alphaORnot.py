String1=input("Enter a String:")
    l=len(String1)
    flag=0
    for i in range(0,l):
        if(String1[i].isalpha()):
            flag=flag+1
    if(flag==0):
        print "The given string has no alphabets"
    elif(flag==l):
        print "The given string contains only alphabets"
    else:
        print "The given string has both alphabets and others"
