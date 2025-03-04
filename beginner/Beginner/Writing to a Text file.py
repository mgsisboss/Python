# Writing to a Text file

# prereq maek sure you create a file in the same directory of your scripts


#file = open("file.txt", "w")  # "r" is for read and "w" is for write
#file.write("python")  #this removes the previous word in the file which was "hello" then it will write what is in the argument "python"
#file.close()  #don't forget this closes file to save, new file will say "file.txt inside the file  is now "python"

file = open("file.txt", "w")  # "r" is for read and "w" is for write
file.write("python\n") #this escape character will allow us to tell python to type to next line
file.write("I am learning how to write to a file")
file.close()  #new file will say "file.txt inside the file  is now "python" on one line and next line "I am learning how to write to a file"