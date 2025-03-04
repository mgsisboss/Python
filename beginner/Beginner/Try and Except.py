# Try and Except

# can let you know if something works example validating a form

#text = input("username: ")  # for this example, I want this string to only be numbers
#number = int(text)
#print(number) # failed "ValueError: invalid literal for int() with base 10: 'hello'   basically it can't convert "hello" into a number without a try and except method

## Lets use the "try and Except method"

text = input("username: ")
try:
    number = int(text)
    print(number)
except:
    print("Invalid Username")  # I typed "hello" and got the response "Invalid Username" as we set our function to only use Numbers via "number = int(text)"
                               # so now if I type a number in the program accepts this as a valid entry instead of crashing the code


