'''
Default constructor
-------------------
We can pass some Object as parameter to the function. In this program, 'getOtherObjectName()' function is illustrating
this. We need not specify which class that object belongs to also, just give a name.

'''

class Student :         # No constructor defined.
    name = "yeti"

    def getOtherObjectName(self, otherObject):
        return otherObject.name


class Car :
    name = "Ritz"



obj1 = Student()
obj2 = Car()

print(obj1.getOtherObjectName(obj2))