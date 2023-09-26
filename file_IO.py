# read (r): This mode opens the file for reading only and gives an error if the file does not exist. This is the default mode if no mode is passed as a parameter.
# write (w): This mode opens the file for writing only and creates a new file if the file does not exist.
# append (a): This mode opens the file for appending only and creates a new file if the file does not exist.
# create (x): This mode creates a file and gives an error if the file already exists.
# text (t): Apart from these modes we also need to specify how the file must be handled. t mode is used to handle text files. t refers to the text mode. There is no difference between r and rt or w and wt since text mode is the default. The default mode is 'r' (open for reading text, synonym of 'rt' ).
# binary (b): used to handle binary files (images, pdfs, etc)


# READING A FILE--->

# f=open('cd7.py','r')    # 'r' is for reading, 'w' is fior writing, 'a' is for appending
# f=open('cd7.py')   # if we don't give any command then it is automatically taken as 'r' as reading 
# print(f)
# text=f.read()
# print(text)
# f.close()

#  WRITING TO A FILE--->

# f=open("myfile.txt","w")  # if we want to write in a already existing file then it will delete the already written notes in that file
# print(f)   # if we want to open a file as writting mode and the file doesn't exist then it will automatically create a new file and then open
# f.write("hey rupam what are you doing?")
# f.close()

#   APPENDING TO A FILE--->
# f=open("myfile.txt","a")
# f.write("\nhey rupam what are you doing?")
# f.close()


with open("myfile.txt","a") as f:         # by using 'with' no need to close the file, it will be automatically closed
    f.write("\nhello how are you?")