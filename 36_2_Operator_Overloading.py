'''
Operator Overloading
--------------------
    Same as Java but while overloading '+', we actually overload '__add__()' method. similarly to over '>', we
    overload '__gt__()' method.
'''


class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # '+' operator overloading
    def __add__(self, otherObject):
        a = self.a + otherObject.a
        b = self.b + otherObject.b
        return A(a,b)


obj1 = A(3,2)
obj2 = A(2,3)


obj3 = obj1 + obj2
print(obj3.a)
print(obj3.b)


