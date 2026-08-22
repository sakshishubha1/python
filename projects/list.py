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
