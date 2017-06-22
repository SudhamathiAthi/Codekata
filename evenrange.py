lower = input("Enter the first no:")
    upper = input("Enter the second no")
    print("Prime numbers between",lower,"and",upper,"are:")
    for num in range(lower,upper + 1):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    print(num)
                else:
                    break
