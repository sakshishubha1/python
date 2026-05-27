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
    choice=int(input("What choice do you want ? 1="))


