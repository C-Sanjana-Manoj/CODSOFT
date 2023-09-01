while True:
    print("Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Remainder")
    ch=int(input("Enter your choice: "))
    a=int(input("Enter 1st number: "))
    b=int(input("Enter 2nd number: "))
    if ch==1:
        r=a+b
        print("Result = ",r)
    elif ch==2:
        r=a-b
        print("Result = ",r)
    elif ch==3:
        r=a*b
        print("Result = ",r)
    elif ch==4:
        if b==0:
            print("Division by zero error!")
        else:
            r=a/b
            print("Result = ",r)
    elif ch==5:
        r=a%b
        print("Result = ",r)
    else:
        print("Invalid Choice!")
    c=input("Do you want to continue (y/n)? ")
    if c=='y' or c=='Y':
        continue
    else:
        break
        
