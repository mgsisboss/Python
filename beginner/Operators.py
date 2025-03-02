# Basic Operators and Input

##  name = "Noah"
##  print (name) # what's inside brackets are called arguments
##

##  print("Hello, What is your name?")
## name = input()
##  print(name)  #this prints line 7, then we enter our name, and then it prints back our name

## this one is more advanced
## print("Hello, What is your name?")
## name = input()
## print("Hello", name)  #adds "Hello" after we give it a name, so if I gave it "Noah" after it asks my name it will say "hello Noah" instead of the previous example of just "Noah"

# operators

#  +      # addition
#  -      # subtraction
#  /      # Division
#  *       # Multiplication

#  num1 = 45
#  num2 = 3
## print(num1 + num2)    #we used the addition operator and created variables for num 1 and num 2 to add 45 + 3 to get 48
## print(num1 - num2)    #we used the subtraction operator and created variables for num 1 and num 2 to add 45 - 3 to get 42
## print(num1 / num2)    #we used the division operator and created variables for num 1 and num 2 to add 45 divided 3 to get 15.0
## print(num1 * num2)    #we used the multiplication operator and created variables for num 1 and num 2 to add 45 multiplied 3 to get 135

## Exponents Operators
##  ** # shows how to do basic exponents
##  // # Integer division operator more to follow later videos

# num1 = 64
# num2 = 10
# 64 // 10  #shows that 10 can go into 64  6 times the // does not give us a remainder
# print (64 // 10 )
# % # this will give us the remainder
# print (64 % 10 ) # remainder 4 after we print

##

# num1 = 45
# num2 = 4
# num3 = num1 ** num2
# print(num3)  #prints 4100625  as 45 exponent 4 is equal to 4100625

## print("Pick a Number: ")
## num1 = input()
## print("pick another number: ")
## num2 = input()

## SUM = num1 + num2  #sum lowercase is a reserver word so we are making a new variable for this example all caps SUM
## print(SUM)   ## good mistake, so for num 1 I put 3, num2 I put 2, when I printed I didn't get 3 + 2 I got 32, below is the fix

##

print("Pick a Number: ")
num1 = input()
print("pick another number: ")
num2 = input()

SUM = int (num1) + int (num2)  #added Integer and brackets around num 1 and num 2 so this should give us the sum of num1 + num2
print(SUM) ## this worked!
