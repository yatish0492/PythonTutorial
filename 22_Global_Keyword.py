'''
global keyword
--------------
'global' keyword is used to specify that a variable is global variable.
'''


a = 10

def f() :
    print(a)        # Output --> 10. It takes the outside variable 'a'
f()


def f() :
    a = 20          # don't think global variable 'a' is changed with value '20'. Once you try to modify it, python
                    # will make it a new local variable 'a'. eventhough both variables are with same name 'a', both
                    # are unrelated to each other.
f()
print(a)            # Output --> 10


# Using 'global' to consider global variable within a function.
def f() :
    global a        # 'global' key word tell python to consider global variable 'a'.
    a = 20          # this will modify the value of global variable.
f()
print(a)            # Output --> 20


# you can use 'global' for only once statement instead of making the reference to global for that variable across full
# function.
def f() :
    a = 20                  # 'a' is a local variable only without any link to global variable 'a'
    globals() ['a'] = 30    # now 'a' is local variable so we cannot us 'a = 30' to set global variable. so we can do this way.
f()
print(a)            # Output --> 30