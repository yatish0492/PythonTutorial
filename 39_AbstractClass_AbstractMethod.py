'''

Abstract Class and Abstract Method
-----------------------------------
    Python doesn't have 'abstract' key word like java.

Abstract Class
--------------
    we need to import 'ABC" class from 'abc' module. 'ABC' means 'Abstract Base Classes'. if we want to declare
    the class as abstract then we need to extend 'ABC' class.

Abstract Method
---------------
    we need to import 'abstractmethod' from 'abc' module. we need to annotate '@abstractmethod' above the method
    which needs to be declared as abstract.

'''

from abc import ABC, abstractmethod

class AbstractClass(ABC) :

    @abstractmethod
    def method1(self) :
        pass                # in python if to mention no definition, we use 'pass' otherwise python gives error.


class ChildClass(AbstractClass) :

    def method1(self) :             # implementing abstract method
        print("The method from child class")



obj = ChildClass()
obj.method1()