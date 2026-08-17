student={
    "name":"Shubha",
    "marks":"95",
    "roll":"21"
}

while True:
    choice=int(input("Enter your choice 1=View Student 2=Update Marks 3=Update Name 4=Add New Field 5= Delete Field 6=Search Field 7=Exit"))
    if choice==1 :
        for key,value in student.items():
            print("----------------")
            print(key,"---",value) 
            print()
    elif choice==2:
        newmarks=input("Enter new marks")
        student["marks"]=newmarks
    elif choice==3:
        newname=int(input("Enter new name"))
        student["name"]=newname
    elif choice==4 :
        field=input("Enter what field you want to add")
        value=input("Enter value you want to add ")
        student[field]=value
    elif choice==5 :
        field1=input("Enter field to delete")
        del student[field1]

    elif choice==6 :
        search=input("Enter value of field you want to search")
        if search in student:
            print(search,":",student[search])
        else:
            print ("not found")
    
    elif choice==7 :
        print('Exiting  program')
        break
    else:
        print("wrong choice")
        continue
    


