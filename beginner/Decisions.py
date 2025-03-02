#Decisions and Conditions

## if x == y:    # don't forget semi colon and indent
   # do this

#age = input("Input your age: ")
#if int(age) == 16:     #Orignally It would not print hey you're 16 without putting "int(age)" in
   # print("hey you're 16")

#age = input("Input your age: ")
#if int(age) >= 16:    # Greater than or equal ">=" can also work for less than or equal "<="
#    print("hey you're 16")


#age = input("Input your age: ")
#if int(age) >= 16:
#    print("hey you're 16")
#else:   #if input is less than 16 below will be printed
#    print("you are younger than 16")


height = input()
if int(height) < 1:
    print("You cannot ride, under 1m")
elif int(height) > 2:     # elif means if the first condition above is false, it will check the next conditions, and it can be going
    print("you cannot ride, over 2m")
else:
    print("you can ride")

