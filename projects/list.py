def add(number):
    add=int(input(enter number to add))
    number.append(add)

def view(number):
    for num in number:
        print(num) 

def remove(number):
    erase=int(inpt("enter number you want to delete"))
    number.delete(remove)

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

while True:
    number=[]
    range=int(input("how many numbers you want to add in in list initially?"))
    for i in range (range):
        num=int(input("enter number"))
        number.append(num)

    choice=int(input("enter what you want to do 1=add,2=view,3=remove,4=largest number,5=smallest number,6-sum,7-avg,8-sort,9-reverse,10-search number,11=count numbers"))
    if choice==1:
        add(number)
    elif choice==2:
        
        view(number)
    elif choice==3:
        remove(number)
    elif choice==4:

    
     




