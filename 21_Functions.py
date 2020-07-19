'''
Functions
---------

NOTE: Since, python is interpreted language, we cannot call a function before function is defined. which will give error.
'''

# if we call 'f1()' here, then it will give error as f1() is not defined yet. we can call it only after definition
# of 'f1()'

# no parameter functions
def f1() :
    print("inside function")
f1()


# parameterized functions
def f2(name , age) :
    print(name + " " + str(age))
f2('yatish', 26)


# parameterized function, mapping parameter name to value.
# This way, we can make sure that we don't pass arguments in incorrect order.
# in below example we might send first parameter as age and second as name which will cause problems.
def f2(name, age) :
    print(name + " " + str(age))
f2(name='yatish',age=26)
f2(age=26, name='yatish')

# parameterized function, with default values
def f2(name , age = 26) :
    print(name + " " + str(age))
f2('yatish')
f2(name='yatish',age=28)


# parameterized function, with variable number of arguments
# ---------------------------------------------------------
# 1) * prefixed variable
# 2) ** prefixed variable
# prefixing '*' to variable name will tells that this variable accepts variable number of arguments with type 'tuple'
# -------------------------------------------------------------------------------------------------------------------
def f3(a, *b) :
    print(a)
    print(b)
f3(1,2,3,4,5,6)    # a = 1, b = (2, 3, 4, 5, 6)
# prefixing '**' to variable name will tells that this variable accepts variable number of arguments with type 'dictionary'
# -------------------------------------------------------------------------------------------------------------------------
# NOTE: you need to send the values as key value pairs.
def f3(a, **b) :
    print(a)
    print(b)
f3(1, name='yatish', age=26)    # a = 1, b = {'name': 'yatish', 'age': 26}


# function with return
def f3(a,b) :
    return a+b
result = f3(1,2)
print(result)


# function with return more than 1 value
def f4(a,b) :
    return a+b,a-b

result_add,result_sub = f4(1,2)
print(result_add)
print(result_sub)

'''
Function Argument types
-----------------------
in python there is no concept like 'pass by value' or 'pass by reference'. If the argument type which we are passing is,
mutable then will act like 'pass by reference'. If the argument type is immutable then it will act like 'pass by value'
'''
# Integer type is immutable, so it acts like 'pass by value'
def f5(a) :
    a = 10
b = 5
f5(b)
print(b)    # Output --> 5. The value is not changed to 10 even though inside function it is set to 10.

# List type is mutable. so it acts like 'pass by reference'
def f6(a) :
    a[0] = 20
    a.append(3)
b = [1,2]
f6(b)
print(b)    # Output --> [20, 2, 3]. The value is changed as per the change done inside the function.



# Default value for parameters.
def f7(a=1):        # '1' is assigned as the default value for parameter 'a'. if we don't pass a value then this default
    print(a)        #   value will be used.
f7()
f7(5)