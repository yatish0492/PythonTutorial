'''
Import Library
--------------
import math --> this will import complete math library.
math.sqrt(25) --> we need to call all functions using 'math'


Importing Library with alias
----------------------------
import math as xyz --> 'math' is imported and assigned 'xyz' as the alias name
math.sqrt(25) --> ERROR : Once you have created alias, then you cannot use 'math',
                  you have to call functions using alias only as shown next
xyz.sqrt(25) --> Perfect/Correct


Importing only few functions/methods in Library
-----------------------------------------------
from math import sqrt,pow --> imports only 'sqrt' and 'pow'.
                              we cannot use any other functions of 'math' like 'floor' etc.
math.sqrt(25) --> ERROR : we need not call 'sqrt' using 'math'. we need call directly 'sqrt' as shown next
sqrt(25) --> Perfect/Correct
pow(2,5) --> perfect/Correct


NOTE : We should not use '_' in file names because when we import that module. if name contains '_', it will not find that file.

'''

