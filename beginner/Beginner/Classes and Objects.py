# Classes and Objects
#x = "string"
#print(type(x))    # x is the object of the  class string
#y = 23
#print(type(y))    # y is the object of the class Integer
#print(x.count("2"))                   # a "." is part of an attribute like  ".count"

class number():
    def __init__(self, num):
        self.var = num

    def display(self, x):
        print(x)

#num = number(23   #<__main__.number object at 0x7ff8dc553e90> this shows where the object is stored, we created the object of the class number
#print(num)

num = number(23)
num.display(num.var)


