'''
Arrays
------
Arrays are not of fixed size unlike how in java it is of fixed size.
Arrays are homogeneous unlike list. It can have elements of only one type.

Arrays is not built-in in python. we need to import it from library.

NOTE: there is no built-in search function in library. we have to iterate manually and search for it.

NOTE: We cannot define multi dimensional array using 'array' package.
'''

from array import *

arr = array('i',[1,2,3,4])  # 1st argument --> type of array, 2nd argument --> values
                            # type of array value 'i' means 'signed int'
                            # please refer to web to see all supported types.

print(arr)                  # Output --> array('i', [1, 2, 3, 4])
print(arr.buffer_info())    # Output --> (4374835376, 4). 1st value --> address of array, 2nd value --> size of array.
print(arr.typecode)         # Output --> i
print(arr[1])               # Output --> 2

arr.append(5)               # adds a new element at the last.

print(arr)                  # Output --> array('i', [1, 2, 3, 4, 5])


# Multi dimensional Array
mularr = array('i',[1,2,3,4],[5,6,7])   # ERROR : TypeError: array() takes at most 2 arguments (3 given)