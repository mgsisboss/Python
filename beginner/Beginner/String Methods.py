# String Methods
from os.path import split

#.strip(), len(), .lower(), .upper(), .split()
#.strip Removes all of the leading and trailing whitespaces from a string

#.strip example
#text = input("input something ")
#print(text.strip())

#len() - stands for length, prints length of list or string
#text = input("input something ")
#print(len(text))  #input a few words and it will give you a word count

#.lower() -  turns everything into lowercase
#text = input("input something ")
#(text.lower())

#.upper() -  turns everything into uppercase
#text = input("input something ")
#print(text.upper())


#.split() -  creates a list out of the string, inside the brackets are called a delimiter
text = input("input something ")
print(text.split("."))   #the period is the delimiter so when you run the script and input you want to input words then a "."
                         # so example  hello.tim.by  will print after input ['hello', 'tim', 'by']       the delimiter "." can be any string I just used "." for this example