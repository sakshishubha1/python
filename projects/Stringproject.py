def upper(name):
    name1= name.upper()
    print("The uppercase of given word is ",name1)

def lower(name):
    print("The lowercase of given word is ",name.lower())
    
def length(name):
    print("The length of word is ",len(name))

def count(name):
    character=input("Enter the character you want to find count of")
    print("The count of the character you entered is",name.count(character))


def replace(name):
    word=input("Enter what world do you want to replace original word with")
    print("the new word is ",name.replace(name,word))
          
def position(name):
    character1=input("Enter character you want to find count of")
    print("The position of given character is ",name.find(character1))

def split(name):
    words=name.split()
    print(words)

def start(name):
    word1=input("enter characters you want to check")
    print("It is ",name.startswith(word1))

def end(name):
    word2=input("enter characters you want to check")
    print("It is ",name.endswith(word2))
    
def comp(name):
    word3=input("Enter word you want to compare with")
    if name==word3:
        print("They are equal")
    
    else:
        print("They are not equal")
    
 
while True:
    name=input("Enter word ")
    choice=int(input("What choice do you want with your word ? 1. Convert to Uppercase 2. Convert to Lowercase 3. Count a Character 4. Replace Word 5. Find Character Position 6. Split Sentence 7. Check Startswith 8. Check Endswith 9. Compare Two Strings   10. Length of String 11. Exit"))
    if choice==1:
        upper(name)
    elif choice==2:
        lower(name)
    elif choice==3:
        count(name)
    elif choice==4:
        replace(name)
    elif choice==5:
        position(name)
    elif choice==6:
        split(name)
    elif choice==7:
        start(name)
    elif choice==8:
        end(name)
    elif choice==9:
        comp(name)
    elif choice==10:
        length(name)
    elif choice==11:
        print("program terminated")
        break
    if choice>11 or choice<1:
        print("Wrong choice")
        continue


     
    







        
    

