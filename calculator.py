from math import pow,sqrt,log,log2,log10,cbrt

print("\t===========WELCOME TO MY CALCULATOR===========\n\n")


tryagain=1 
maintry=1
while(maintry==1):
    while(tryagain ==1):
        x=0
        y=0
        opt=0
        print("1) DIVISION\n2) MULTIPLICATION\n3) ADDITION\n4)SUBTRACTION")
        print("5) SQUARE\n6) SQUARE ROOT\n7) CUBE\n8) CUBE ROOT\n9) LOG BASE 10")
        print("10) LOG BASE 2\n11) NATURAL LOG\n")
        opt=int(input("Enter operation:"))
        if(opt>=1 and opt<=4):
            x=int(input("Enter First Number: "))
            y=int(input("Enter Second Number: "))
            tryagain = 0
        elif(opt>=5 and opt <=11):
            tryagain = 0
            x=int(input("Enter The Number: "))
        else:
             tryagain=1
    
    match opt:
        case 1:
            if(x>y):
                print("Quotient:",x/y,'\nRemainder:',x%y)
            elif(x<y):
                print("Quotient:",y/x,"\nRemainder:",y%x)
            elif(x==y):
                print("Quotient: 1",'\nRemainder: 0')
            else:
                print("Somthing Went Wrong!!")
        case 2:
           print("product:",x*y)
        case 3:
            print("product:",x+y)
        case 4:
            if(x>y):
                print("Difference:",x-y)
            elif(x<y):
                print("Difference:",y-x)
            elif(x==y):
                print("Difference: 0")
            else:
                print("Something Went Wrong!!")
        case 5:
            print("The square:",pow(x,2))
        case 6:
            print("The square root:",sqrt(x))
        case 7:
            print("The cube:",pow(x,3))
        case 8:
            print("The cube root:",cbrt(x))
        case 9:
            print("The common log:",log10(x))
        case 10:
            print("The binary log:",log2(x))
        case 11:
            print("The naturall log:",log(x))
        case _:
                print("Something Went Wrong!!")
    maintry=int(input("WOULD YOU LIKE TO CONTINUE USING THE CALCULATOR?\n\t1->YES\n\t2->NO"))
    tryagain=1
    
