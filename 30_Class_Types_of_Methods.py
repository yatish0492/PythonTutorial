'''
Types of Methods in Class
-------------------------
1) Instance methods
2) Class methods
3) Static methods


NOTE : the Getter methods are called as Accessor methods
NOTE : the Setter methods are called as Mutator methods

NOTE : In case of variable, both static and class variable are same only but class method and static methods are not same.

'''


class Student :

    school = "VMHS"

    def __init__(self, name):
        self.name = name

    # instance method
    # ---------------
    # instance methods are the methods which deals with instance variables.
    def displayInstanceVariableStudentName(self):
        print("The Student name is - " + self.name)

    # Class Method
    # -------------
    @classmethod                                # '@classmethod' specifies to python that this method uses only static/Class
    def displayStaticOrClassVariable(self):     #       variables, so that we can call this function using just class. like
        print("The school name is - " + self.school)#   'Student.displayStaticOrClassVariable()'. If this annotation is
                                                #       not mentioned. then if we call this method using just class
                                                #       then python gives error.

    # So i can just specify any function with @classmethod and call it using class name. Consider i put this annotation
    # to instance method 'displayInstanceVariableStudentName()'. how does it get value of 'Self.name' since we are not
    # creating a object and calling it by class?
    # Python will silently give error that 'self.name' not defined at run time :P


    # static method
    # -------------
    # static methods are those methods which doesn't use any data member/ variables in it. eg: you can use these methods
    #       if you want to just print some info to log.
    #
    # NOTE : we cannot even give 'self' as parameter. if we give it then python throws error.
    @staticmethod               # If you don't mention this annotation, then you will not be able to call this method
    def thisIsStaticMethod():   # using class 'Student'
        print("This is a static method")


    # If we want to do something with the class/static variable then we have to use '@classmethod' and we need to
    # access them using 'cls'. 'self' is not allowed in methods with '@classmethod'
    @classmethod
    def updateStaticVariable(cls):
        cls.school = "seshadripuram"
        return cls.school



obj = Student("yatish")

obj.displayInstanceVariableStudentName()        # Output --> The Student name is - yatish

obj.displayStaticOrClassVariable()              # Output --> The school name is - VMHS

# Calling class method using class name. No need to even send any object as argument for 'self'
Student.displayStaticOrClassVariable()          # Output --> The school name is - VMHS

# Calling static method using class name.
Student.thisIsStaticMethod()                    # Output --> This is a static method


Student.updateStaticVariable()

