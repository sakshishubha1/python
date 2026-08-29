def add(number):
    add=int(input("enter number to add"))
    number.append(add)

def view(number):
    for num in number:
        print(num) 

def remove(number):
    erase=int(input("enter number you want to delete"))
    if erase in number:
         number.remove(erase)
    else:
        print("number not found")
   

def maximum(number):
    print("the max of number is ",max(number))

def minimum(number):
    print("the minimum number is",min(number))

def avg(number):
    print("the average is ",sum(number)/len(number))
    
def sort(number):
    number.sort()
    print("the sorted version is")
    for num in number:
        print(num)

def reverse(number):
    number.reverse()
    print("the reversed list is ")
    for num in number:
        print(num)

def search(number):
    search=int(input("enter number to find"))
    if search in number:
        print("number found")

def count(number):
    print("the number of numbers in list is ",len(number))

def s(number):
    sum1=sum(number)
    print("the sum is ",sum1)
    


number=[]
while True:
    choice = int(input("""1=add, 2=view, 3=remove, 4=max, 5=min,6=sum, 7=avg, 8=sort, 9=reverse,10=search, 11=count, 12=exit: """))
    if choice == 1:
        add(number)
    elif choice == 2:
        view(number)
    elif choice == 3:
        remove(number)
    elif choice == 4:
        maximum(number)
    elif choice == 5:
        minimum(number)
    elif choice == 6:
        s(number)
    elif choice == 7:
        avg(number)
    elif choice == 8:
        sort(number)
    elif choice == 9:
        reverse(number)
    elif choice == 10:
        search(number)
    elif choice == 11:
        count(number)
    elif choice == 12:
        print("Program terminated")
        break
    



     




