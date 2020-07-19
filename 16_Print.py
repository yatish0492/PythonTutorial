'''
print
'''


# print() is equivalent to println() in java. Automatically '\n' will be added at last
print("this is println ")
print("this is println ")


# How to achieve print() of java. we need to explicitly specify what should be the end string by providing 'end='
print("this is print() functionality",end="")
print("this is print() functionality",end="")


# printing a string along with number
a = 10
print("The count number is : " + a)     # ERROR: can only concatenate str (not "int") to str. concatination accepts
                                        # only strings with '+' operator. so we need to manually convert other types
                                        # types to string using 'str()' and then use it.
print("The count number is : " + str(a))
# Or
print("The count number is : {}".format(a))
b = 20
print("The count number is : {} and b = {}".format(a,b))
