# Optional Parameters

#def func(x): #recap of a basic function
 #   print(x)
#func("hello")


#def func(x, text):
#     print(x)
#    if text == "1":
#   #     print("text is 1")
#   else:
#       print("text is not 1")

#func("noah", "1")  #text is 1
#func("noah", "2")  #text is not 1


# lets improve this by declaring text

def func(x, text="2"):
     print(x)
     if text == "1":
        print("text is 1")
     else:
       print("text is not 1")
func("noah")  # we get this result     noah
                                      #text is not 1
                                  #because the default value of "text" is "2' unless specified
                                  # its good to set optional parameters if you do not want to type the same parameter in multiple times


