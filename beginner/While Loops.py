# While Loops
# Syntax: while condition == true:
#            do this
#             break

#loop = True  #adding this so we don't have to specific == true

#while loop:
#    name = input("Insert Something: ")
#   if name == "stop":
#        loop = False
#        break    #program runs "Insert something" you can add as much as you want until you type "stop"


loop = True

while loop:
    name = input("Insert Something: ")
    if name == "stop":
        break  # you do not need to have loop == false from previous, looks cleaner, and can continue what is outside the code
               # A "while loop" in programming repeats a block of code as long as a specified condition remains true, meaning
                # you don't necessarily know how many times it will run beforehand, while a "for loop" is used when you know exactly how many times you want to repeat the code, typically iterating through a set number of items in a sequence like an array or list.


