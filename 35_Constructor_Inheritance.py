'''

Constructor order in Inheritance
---------------------------------
Unlike Java, the parent class constructors are not called in python. if we want then we need to manually call the
parent constructor using 'super().__init__()'.

NOTE: we know that python supports 'Multiple Inheritance' so conflict in calling which parent class constructor
        occurs if we use 'super().__init__()'. to see how it works in this case refer to 'gObj = G()' in this
        program.

'''


class A:
    def __init__(self):
        print("Constructor of A")

class B(A):
    def __init__(self):
        print("Constructor of B")



bObj = B()  # it calls only constructor of 'B' and constructor of 'A' which is its parent is not called. We need to
            # call parent constructor manually using 'Super().__init__()' as we are doing in 'D' class below




class C:
    def __init__(self):
        print("Constructor of C")

class D(C):
    def __init__(self):
        super().__init__()      # we are calling parent constructor manually
        print("Constructor of D")


dObj = D()  # this will call the parent class constructor as we are manually it in 'D' class constructor.



class E:
    def __init__(self):
        print("Constructor of E")

class F:
    def __init__(self):
        print("Constructor of F")

class G(E,F):
    def __init__(self):
        super().__init__()
        print("Constructor of G")


gObj = G()  # we are calling 'super().__init__()' in 'G' class constructor which inherits 'E' and 'F' in this case
            # we have a conflict like which parent class constructor to call in this case it will call the first
            # class constructor in the order, which is 'E' In 'G(E,F).