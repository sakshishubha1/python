def add(a, b):
    print("The sum is", a + b)


def sub(a, b):
    print("The result is", a - b)


def multiply(a, b):
    print("The product is", a * b)


def division(a, b):
    print("The result is", a / b)


while True:
    x = int(input("Enter first number"))
    y = int(input("Enter second number"))

    print("Enter choice")
    print("1 Add")
    print("2 subtract")
    print("3 Multiply")
    print("4 Division")
    print("5 exit")
    choice=int(input())
    

    if choice==1:
        add(x,y)
        
    elif choice==2:
        sub(x,y)
    
    elif choice==3:
        multiply(x,y)
    
    elif choice==4:
        if y==0:
            print("division not possible")
        else:
            division(x,y)
    elif choice==5:
        print("Program terminated")
        break
    if choice>5 or choice<1: 
        print("Wrong choice")
        continue