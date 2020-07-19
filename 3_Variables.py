'''
Variables in Python
-------------------
You do not need to declare variables before using them, or declare their type. Every variable in Python is an object.
'''


a = 10


# Getting address of the variable. 'id(<VARIABLE>)' is the function used to fetch address of the variable.
print(id(a))

'''
Python is more memory efficient. It is like string literals in java. See example below to understand.
'''
b = 10
c = 10
print(id(b))    # Output --> 4386278864
print(id(c))    # Output --> 4386278864, both variables 'b' and 'c' are pointing to the same memory address
                # when we created variable 'c' and assign it '10'. Instead of
                # allocating a new space and storing '10' in it, python will check if already
                # there is a space/variable holding same value and point it to same memory address.
print(id(10))   # Output --> 4386278864, same address as that of 'a','b','c' variables address.
                # we can get the address of the value as well since there cannot be more than one
                # address/space with same value.


# When value of a variable is changed, it doesn't change the value in the same address/space. It will create a new
# space and store new value and assign that new address/space and assign that address/space to the variable.
d = 10
print(id(d))    # Output --> 4386278864
d = 20
print(id(d))    # Output --> 4323139344. the address of 'd' has changed since '10' was not changed to '20' in same
                # address/space '4386278864'. python created a new address/space


# It is not pass/assignment by reference
e = 10
f = e
e = 20
print(f)        # Output --> 10. changing value of 'e' doesn't change value of 'f' as it is not assignment by reference.
                # even though, when 'e' is assigned to 'f', 'f' will be pointing to the same address/space. when 'e' is
                # changed with '20' only 'e' address/value will be changed but not 'f' address/value.


# finding type of an variable. 'type(<VARIABLE>)' function is used.
g = 10
print(type(g))  # Output --> <class 'int'>
h = 10.5
print(type(h))  # Output --> <class 'float'>
i = "yatish"
print(type(i))  # Output --> <class 'str'>







