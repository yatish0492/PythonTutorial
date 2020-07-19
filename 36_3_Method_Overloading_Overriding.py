'''

Method Overloading
------------------
    Python doesn't support Method Overloading. Even if we do try to override a method, then the last method definition
    with same name will be considered and all previous method definitions will be ignored.


Method Overriding
-----------------
    It is same as that of java. child class method will override parent class method.

'''

class MethodOverloading:
    def method1(self):          # This method will be ignored and replaced with next method. it doesn't take overloading.
        print("method1")

    def method1(self):          # whenever we call 'method1()'. this method will be called. previous one will be ignored.
        print("Overloaded method1")     # basically its like overriding previous 'method1()'

    def method2(self, a):
        print("parameterized method2")

    def method2(self):          # Similarly this method will be considered and previous 'method2()' will be ignored.
        print("no parameter method2")   # even if we call 'method2(5)' it will give error because previous method with
                                        # parameter is ignored or overridden by this so.

obj1 = MethodOverloading()
obj1.method1()
obj1.method2()


