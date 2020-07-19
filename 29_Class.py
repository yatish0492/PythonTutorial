'''
OOP in python
-------------
Supports Class

What will the size of the object?
THe size is decided based on the number of variables/data_members

* Static/Class Variables will be stored in class namespace
* instance Variables will be stored in instance namespace

'''


class A :

    c = 3                      # Declaring a static variable
    #d                          # you cannot simply declare without defining value because it is static.

    '''def __init__(self):      # We cannot give multiple constructors/__init__() like non parameterised and parameterised.
        self.a = 10
        self.b = "yatish"'''

    def __init__(self, a, b):
        self.a = a              # variable name without any prefix is considered as public data member
        self.b = b
        self._d = 6             # variable name with prefix '_' is considered as protected data member
        self.__e = 7            # variable name with prefix '__' is considered as private data member
        #self.c = 100            # we can change the static variable/data_member

    def printMembersOfClass(self):
        #print("a --> " + str(a))       # we cannot reference a data member of the class without using 'self.' as shown in next line
        print("a --> " + str(self.a))
        print("b --> " + str(self.b))
        print("c --> " + str(self.c))   # even static data member of class needs to be accessed using 'self.
        print("d --> " + str(self._d))
        print("e --> " + str(self.__e))

    def setPrivateVariable__e(self,e):
        self.__e = e


obj = A(1,2)           # no need of of 'new' keyword while creating objects.

obj.a = 4          # Outside also we can easily modify the data members of the object.
obj.c = 5           # If we change the static/class variable using object then that value will be specific to this object,
                    # For other objects still the value be 3

A.c = 5            # If we change the static/class variable using class then that value will be changed for any other
                   # objects created.

obj._d = 8        # we can set the protected data members this way. The value will be changed to 8 for this object.
obj.__e = 9       # setting private data members will not give any error, but the variable will not be set with this value.
                  # still the value of '__e' will remain same '7'

obj.setPrivateVariable__e(9)    # only the function within class can set the private variables/data_members

obj.printMembersOfClass()
A.printMembersOfClass(obj)

print("-------------")
obj1 = A(20,30)
A.a = 55         # if we change a instance variable/data_member using class name then there will be no error but
                 # the value will not be set. the value will still remain '20'


obj1.printMembersOfClass()

print("-------------")
obj2 = A(30,40)
obj2.printMembersOfClass()