'''

File Handling
-------------

'''

fileRead = open('Resources/data.txt', 'r')  # opening the file in read mode. we can use 'rb' as mode as well which
                                            # means it reads the file in binary mode.

print(fileRead)

print(fileRead.readline())     # Read one line. it is like iterator's 'next', next time you execute 'readline()'. it will
                            # print next line. in this code we are executing 'readlines()' next so it will read all the
                            # lines next to the line read here.

print(fileRead.readlines())    # Read all the lines

print(fileRead.readline(4))     # read the line. only 4 characters. In this code as we already read all the lines, this
                            # gives empty as there is no next line.

print(fileRead.readline(), end="#")  # This will print '#' at the end of the line.



fileWrite = open('Resources/data.txt', 'w')     # opening the file in 'write' mode.

fileWrite.write("Gagan")                        # writing to the file
fileWrite.writelines("Jeshwanth")               # same as 'write()' it doesn't add new line character at last.


