#Reading from a Text file

# prereq maek sure you create a file in the same directory of your scripts


file = open("file.txt", "r")   #this opens and read mode the file
f = file.readlines()
print(f)   # prints ['Noah\n', 'Happy\n', 'bday\n', 'wow!\n']    \n is an escape character because its end of the line

####  to remove the "\n" we will make a for loop to remove"

#newList = []   #create a new list declare a variable can be anything for our example "newList"
#for line in f:   #create a for loop in the line
#    newList.append(line [:-1])    # use slice oeprator, it will take all of line minus last character "-1 " will remove the last character and append the list
#print(newList)   #prints ['Noah', 'Happy', 'bday', 'wow!']

#Strip method to remove "\n"

newList = []
for line in f:
    newList.append(line.strip())
    print(newList) # Prints  ['Noah', 'Happy', 'bday', 'wow!']



