#Chained Conditionals and Nested Statements

#Recap
#x = 2
#y = 3
#x == y  #will give us False because 2 does not equal 3

#x = 2
#y = 3
#if x == y and x + y == 5:
#   print("ran")   #nothing will run because "and" statement needs both statements to be true

#####

#x = 2
#y = 3
#if x == y or x + y == 5:   #or only one statement needs to be True, "ran" will now print
#    print("ran")

#####

#x = 2
#y = 3
#if not (x == y or x + y == 5):   # not reverses whats in the statement presented since  " (x == y or x + y == 5):" is a True statement adding "not" before it now makes it false, so the else statement will print ":("
#    print("ran")
#else:
#    print(" :( ")



#Nested if Statements

x = 2    #if  you change these variables you will get different results refer to video
y = 3

if x == 2:
    if y == 3:
        print("x = 2, y = 3")
    else:
        print("x = 2, y != 3")
else:
    print(" x != 2")






