# Using .count() and .find()

#.find(), .count()

#. find

#string = "hello"
#print(string.find("l"))   # will find what is in the indice, so this example the "l"  in hello, is "2" because "h" is "0", "e" is 1 and "l" is "2"
#print(string.find("o"))   # will find what is in the indice, so this example the "o"  in hello, is "4" because "h" is "0", "e" is 1, "l" is "2", "l: is "3" and "o" is "4"
#print(string.find("7"))   # we will get the response "-1" if something is not in the string, "7" is not in the string hello


#.count
#string = "hello"
#print(string.count("l"))  # we have 2 "l" in "hello" so it should print 2


string = "wwewdwkdwkdwjdwhdhwdw"
print(string.count("w"))  # we have 9 "w" in this string
print(string.count("z"))  # we have 0 "z" in this string
print(string.find("w"))  # we found 0 "w" in this string because the string starts with "w"


