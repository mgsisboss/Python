#Global vs Local Variables
from pickle import GLOBAL

# Local Variables

#var = 9     #Global variable
#loop = True # Global variable

#def func(x):
#     newVar = 7  #Local variables

 #    if x == 5:
 #        return newVar

#print(newVar)  #NameError: name 'newVar' is not defined, Why?
               # because newVar is a local variable to the function "func"    "print(newVar} will need to be inside the function so line 9 should print 7

#print(var) #Prints 9 because var is a Global variable



#change global variable within a local variable

#var = 9     #Global variable
#loop = True # Global variable

#def func(x):
 #   var = 10
#    newVar = 7  #Local variables

#    if x == 5:
#        return newVar


#print(var) # will print 9 because It's global and not 10 as that's local to change we need to add the "Global var" inside the function

var = 9     #Global variable
loop = True # Global variable

def func(x):
    global var #ADDED
    var = 11    # Local Variable
    newVar = 7  #Local variable
    if x == 5:
        return newVar

func(var)
print(var)  #prints 11 because we added global var on line 41,and changed the global variable of "var" from 9 to 11


