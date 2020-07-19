'''
Inner Class
-----------
It is similar to Java, In outer class, if we need to access inner class members then we need to create object of inner
    class and access them.
    But one difference is that inner class doesn't have access to outer class members like java.
'''

class Student:
    def __init__(self):
        self.rollNumber = 1

    def accessingChildClassMember(self):
        obj = self.Laptop()
        print(obj.brand)                # accessing inner class member using inner class object.



    class Laptop:
        def __init__(self):
            self.brand = "HP"

        def accessingParentClassMember(self):
            print(rollNumber)      # this gives error as we cannot access out class members like java. even using
                                    # 'self.rollNumber' doesn't help


studentObj = Student()
laptopObj = Student.Laptop()

studentObj.accessingChildClassMember()
laptopObj.accessingParentClassMember()