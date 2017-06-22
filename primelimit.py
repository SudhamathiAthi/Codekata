    sam=input("Enter the range no1:")
    sam1=input("Enter the range no2:")
    for i in range(sam,sam1+1):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    print(num,"is not a prime number")
                    print(i,"times",num//i,"is",num)
                    break
                else:
                    print(num,"is a prime number")
        else:
            print(num,"is not a prime number")
