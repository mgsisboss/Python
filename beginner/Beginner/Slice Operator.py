#Slice Operator
fruits = ["apple", "pear", "strawberrys"]
text = "Hello I like Python"


#print(text[0:5])   #slice Operator ":" works similar to the in range function, prints Hello, because that's 0,5, for "hello" in the text, line 3
#print(text[:5]) # if you are unsure of where to start you can leave the first argument as nothing and state the end, so 5, and it will print hello
#print(text[1:])   # leaving closing argument blank will display everything following your initial entry, so putting 1 in will print "ello I like Python"

#print(text[::2])  #additional colons "::" add a step feature, the "2" skips every two letter, prints "HloIlk yhn"
#print(text[::3])  #additional colons "::" add a step feature, the "3" skips every three letter, prints "HlIi tn"

#print(fruits[1:]) # prints  ['pear', 'strawberrys']

#Insert Function

#fruits.append("b")  #recap adds to end of list, but only lets us append to end of list, what if we want "b" somewhere else in the list, slice operator can help
#print(fruits)

fruits[1:1] = "b"
print(fruits)  # Prints ['apple', 'b', 'pear', 'strawberrys']