student={
    "name":"Shubha",
    "marks":"95",
    "roll":"21"
}

while True:
    choice=int(input("Enter your choice 1=View Student 2=Update Marks 3=Update Name 4=Add New Field 5= Delete Field 6=Search Field 7=Exit"))
    if(choice==1):
        for key,value in student.items():
            print("----------------")
            print(key,"---",value) 
            print()
    elif(choice==2):
        newmarks=int(input("Enter new marks"))
        student["marks"]=newmarks
    elif(choice==3):
        newname=int(input("Enter new name"))
        student["name"]=newname
    

