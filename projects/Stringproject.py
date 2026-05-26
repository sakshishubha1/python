def upper(name):
    name1= name.upper()
    print("The uppercase of given word is ",name1)

def lower(name):
    print("The lowercase of given word is ",name.lower())
    
def length(name):
    print("The length of word is ",len(name))

def count(name):
    character=char(input("Enter the character you want to find count of"))
    print("The count of the character you entered is",name.count(character))


def replace(name):
    word=str(input("Enter what world do you want to replace original word with"))
    print("the new word is ",name.replace(name,word))
          
def position(name):
    character1=str(input("Enter character you want to find count of"))
    

