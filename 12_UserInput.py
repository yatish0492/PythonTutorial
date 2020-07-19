'''
'input' is the method used to get user input
'''

a = input("Please type something!!! : ")    # Once interpretor interpretes this like it wait there for usr input in console.
print(a)

b = input("Waiting for your input : ")[0]   # even if input is 100 characters, only 1st character will be read and assigned to 'b'
print(b)


c = eval(input("Enter a expression : "))    # it will evaluate the expression inputted. eg: input --> '2+5', 'c' will be assigned '7'
print(c)                                    # If don't enter proper expression then exception will occur.