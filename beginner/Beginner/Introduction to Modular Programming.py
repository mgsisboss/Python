#  Introduction to Modular Programming
#import math   # there are many modules you can import in python this is the math module, you are able to create your own module to import as well

#math .  #the "." will show you whats in the module that we could not see before without importing the math module

#print(math.pi)  # Prints pi 3.141592653589793

#create a file in same directory called "myModule.py"
# within this script I made the script:
# def myFunc(X):
#     return x + 5


# then we want to import our new module "myModule"

import myModule
print(myModule.myFunc(4))  #prints 9 because our function "myModule is x + 5, for this x = (4) + 5 = 9

# these modules are reusable for future  use, python has a list of modules on their site like pygame is a popular module for game dev


