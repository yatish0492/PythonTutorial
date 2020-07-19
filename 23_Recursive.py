'''
Recursive Functions
-------------------
Same as how it is in java but in python, by default the default recursive limit is 1000, which means, if function
can be called recursively for 1000 max and if it calls after 1000 times then python will throw an error -
'RecursionError: maximum recursion depth exceeded while calling a Python object'

we can override the recursive limit by importing 'sys' library and calling 'sys.setrecursionlimit()'

'''

import sys

print(sys.getrecursionlimit())          # Output --> 1000

sys.setrecursionlimit(2000)             # Sets the recursive limit from 1000 to 200.

def f() :
    print("inside function")
    f()                                 # Recursive call

f()