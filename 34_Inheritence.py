'''

Inheritance
-----------
Same as Java But it does support 'Single Level Inheritance' and 'Multi Level Inheritance' But unlike java, we will be
    able to do 'Multiple Inheritance'.

NOTE : we do inheritance by syntax '()' We mention parent class within it.

If we do 'Multiple Inheritance' in python then how does it handle conflicting methods of parents?
    if there are conflicting methods then it will take the method from the first class in the order which have that
    method.

'''


class A:
    def aMethod(self):
        print("class A method")
    def conflictMethod(self):
        print("class A method")


class B(A):
    def bMethod(self):
        print("class B method")


class C:
    def conflictMethod(self):
        print("class C method")


class D(C,A):
    def dMethod(self):
        print("class D method")



bObj = B()
dObj = D()


bObj.aMethod()      # calling the method inherited from the parent class 'A'
dObj.conflictMethod()  # we are calling the method 'conflictMethod()' which is present in both 'A' and 'C' class which
                        # are parent classes of 'D'. As class 'C' is first in the order 'D(C,A). it will call the
                        # method 'conflictMethod' of class 'C' instead of 'A'