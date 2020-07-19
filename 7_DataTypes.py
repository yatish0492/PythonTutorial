'''
Following are the data types as follows,
1) None
2) Numeric
    a) int
    b) float
    c) complex
    d) bool
3) List
4) Set
5) Tuple
6) String
7) Range
8) Dictionary



'''

'''
None
----
This is same 'null' in java. In python, instead of 'null' we call it as 'none'
'''
#a
# print(type(a))   --> This will give error as we are trying to pass 'none' to a function. which is like passing null to a function.


'''
Numeric
-------
we know 'int' and 'float', 'bool' it is same a boolean and 'complex'

NOTE: bool values are case sensitive values are 'True' and 'False'. 'true' or 'false' will give error as first character
       needs to be capital as it is case sensitive.

lets see complex type, Complex numbers are specified as '<real part>+<imaginary part>j'. eg: 2+8j. I remember doing this kind of
mathematical calculations in college, don't remember how to solve these need to check.
'''
b = 5 + 6j      # Complex type.
print(b)        # Output --> (5+6j)
c = float(5)    # 'float()' function to convert to 'float'
print(c)        # Output --> 5.0
d = int(5.25)   # 'int()' function to convert to 'int'
print(d)        # Output --> 5
e = complex(1,9)# 'complex()' function to convert to 'complex()'. it accepts 2 args, 1st is 'real part' and 2nd is 'imaginary part'
print(e)        # Output --> (1+9j)
f = bool(1)     # 'bool()' function to convert to 'bool'
print(f)        # Output --> False
g = int(True)   # 'int()' function to convert to 'int'
print(g)        # Output --> 1


'''
List
'''
print(type([1,"uatish",3.5]))   # Output --> <class 'list'>


'''
Set
'''
print(type({1,"yatish",3.5}))   # Output --> <class 'set'>


'''
Tuple
'''
print(type((1,"yatish",3.5)))   # Output --> <class 'tuple'>


'''
String
'''
print(type("yatish"))           # Output --> <class 'str'>


'''
Range
-----
Range type contains ranges like 0 to n. eg: 0 to 100.

What is the use of Range?
consider sometimes you want to have a list of even numbers till 10 thousand, then instead of writing a code to create
a list and populate it with a for loop, you can easily use range like this 'range(0,10000,2)' 
'''
i = range(10)
print(i)                # Output --> range(0, 10)
print(type(i))          # Output --> <class 'range'>
j = list(i)             # Converting range into a list
print(j)                # Output --> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(0,10,2)))  # Output --> [0, 2, 4, 6, 8]. it takes all numbers form 0 to 10 and takes only indexes with interval 2.
print(list(range(0,10,3)))  # Output --> [0, 3, 6, 9]. it takes all numbers form 0 to 10 and takes only indexes with interval 3.


'''
Dictionary
----------
Dictionary is same as map in java.
Dictionary is represented by {} having values as 'key:value'

NOTE: '.put()' is not supported. instead you need to use '.update'
'''
k = {'name':'yatish',2 : 'something', 3 : 45}
print(k)                    # Output --> {'name': 'yatish', 2: 'something', 3: 45}
print(k.get(2))             # Output --> something
print(k['name'])            # Output --> yatish. We can also do 'get' by giving the key like a index as shown.
print(k.keys())             # Output --> dict_keys(['name', 2, 3])
print(k.values())           # Output --> dict_values(['yatish', 'something', 45])
k.update({'Mother':'Shobha'})       # update() will first check if key exists, if exists then update value other add new entry.
k.update({2 : 'heterogeneous'})
k['Father'] = 'ChanneGowda'         # instead of 'update()' we can do it this index way as well.
k[3] = 85
print(k)                    # Output --> {'name': 'yatish', 2: 'heterogeneous', 3: 85, 'Mother': 'Shobha', 'Father': 'ChanneGowda'}









