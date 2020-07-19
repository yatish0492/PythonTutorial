'''
Modules
-------
In python each python file is considered as a module.

In java, we need not specify import of the package if the class we use is within same package. But in python whether if
the file we refer is in same directory/package then also we need to specify 'import' of that.

NOTE : We should not use '_' in file names because when we import that module. if name contains '_', it will not find that file.

'''


# When we import any module. python will literally execute that file/module. In this case, 'Addition.py' have
# print statement "Start of Addition Module" and then definition of function 'addition()'.
# So in below statement, we import 'Addition.py' so it is executed and prints "Start of Addition Module"
import Addition as add          # Output --> "Start of Addition Module"

# NOTE : due to this we should always put whatever we want to do within function definitions instead of putting it
#        outside. because when we import a module, we don't want something to be executed in that file, we just
#        import that module in our file.

print(add.addition(5, 3))       # Output --> 8


import packageY.Substraction as sub     # Importing a module within different package. Syntax --> 'Package.module'

print(sub.substraction(5,3))    # Output --> 2


