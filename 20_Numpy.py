'''
Numpy library
-------------

Why do we need numpy library?
It provides lot of things among which one is 'multi-dimensional' array.

functions defined in numpy
--------------------------
1) array()
2) matrix()
3) linespace()
4) logspace()
5) arange()
6) zeroes()
7) ones()

NOTE: all the numpy functions return type is '<class 'numpy.ndarray'>'


'''

from numpy import *

'''
array()
-------
Syntax --> array(<ELEMENTS>,type)
'''
arr = array([1,2,3],int)
print(arr)                  # Output --> [1 2 3]
arr1 = array([1,2,3])       # we can skip 'type' python will figure out by itself.
arr2 = array([1,2,3.5])     # pythong will consider 'float' as type for all as all will be type casted to float.
print(arr2)                 # Output --> [1.  2.  3.5]. as we can see all elements are converted to float.

print(type(arr2))           # Output --> <class 'numpy.ndarray'>
print(arr2.dtype)           # Output --> float64. '.dtype' property gives the type of values in array

arr1 = array([1,1,1])
print(arr1 + 5)             # Output --> [6 6 6]. adds each element of array with 5

arr1 = array([1,1,1])
arr2 = array([3,3,3])
print(arr1 + arr2)          # Output --> [4 4 4]. adds each element of arr1 with arr2.
                            # NOTE : if arrays sizes doesn't match then it will give error.

print(concatenate([arr1,arr2])) # Output --> [1 1 1 3 3 3]. concatinates both arrays.

arr1 = array([1,2,3])
print(sin(arr1))            # Output -->[0.84147098 0.90929743 0.14112001]. give array of sin(x) of each element.
print(cos(arr1))            # Output -->[ 0.54030231 -0.41614684 -0.9899925 ]. give array of cos(x) of each element.
print(sum(arr1))            # Output --> 6. gives sum of all elements in the array
print(sqrt(arr1))           # Output --> [1.         1.41421356 1.73205081]. gives array of square root of each element.
print(log(arr1))            # Output --> [0.         0.69314718 1.09861229]. gives array of log of each element.
print(min(arr1))            # Output --> 1. gives minimum element of array elements.
print(max(arr1))            # Output --> 3. gives maximum element of array elements.


# Copying array
# -------------
# There are 2 types of copying array as follows,
# 1) Shallow copy
# 2) Deep copy
# Shallow Copy
# ------------
arr1 = array([1,2,3])
arr2 = arr1     # one more way is --> 'arr2 = arr1.view()'
arr1[0] = 5
print(arr2)     # Output --> [5 2 3]. Both arr1 and arr2 point to same array so changing arr1 is reflected in arr2.
# Deep Copy
# ---------
arr1 = array([1,2,3])
arr2 = arr1.copy()     # Deep copy
arr1[0] = 5
print(arr2)     # Output --> [1 2 3]. changing arr1 doesn't affect arr2.


# Multi-Dimensional Array
# -----------------------
arr1 = array([[1,2,3],[4,5,6]])
arr1[0][0] = 9
print(arr1.size)                    # Output --> 6.
arr1 = array([[1,2,3],[4,5,6]])
arr2 = arr1.flatten()               # 'flatten()' will make multi-dimensional to single array.
print(arr2)                         # Output --> [1 2 3 4 5 6].
arr3 = arr2.reshape(2,3)            # 'reshape(x,y)' will convert single array to multi-dimensional with 2 row, 3 column
print(arr3)                         # Output --> [[1 2 3]
                                    #             [4 5 6]]
arr1 = array([1,2,3,4,5,6,7,8])
arr4 = arr1.reshape(2,2,2)          # this will create 3D array of size 2,2,2
print(arr4)                         # Output --> [[[1 2]
                                    #               [3 4]]
                                    #
                                    #               [[5 6]
                                    #                   [7 8]]]

'''
matrix()
--------
matrix() is similar to Multi-Dimensional Array. But this provides additional functionalities like 'diagonal' etc.

NOTE: it will be deprecated in sometime.
'''
mat = matrix('1,2,3;4,5,6')
mat1 = matrix('1,2,3;4,5,6')
print(mat)
print(mat.max())
print(diagonal(mat))
print(mat + mat1)


'''
linspace()
-----------
Syntax --> linspace(<Start_Num>, <End_Num>, <Num_of_Parts>)

linspace() is similar to range but, within this range, the numbers will be partitioned based on 'Num_of_Parts' argument.
'End_Num' is inclusive here.

NOTE: default value of 'Num_of_Parts' is 50

NOTE: the result will always be float values.
'''
a = linspace(0,5,6)         # 0 to 5 will be divided into 5 parts. please find below result.
print(a)                    # Output --> [0. 1. 2. 3. 4. 5.]
a = linspace(0,5,12)        # 0 to 5 will be divided into 12 parts. please find below result.
print(a)  # Output --> [0.         0.45454545 0.90909091 1.36363636 1.81818182 2.27272727 2.72727273 3.18181818 3.63636364 4.09090909 4.54545455 5.        ]

a = linspace(0,5)           # if, 3rd argument is not given then it will take default value 50. 0 to 5 will be divided into 50 parts.

print(type(a))              # Output --> <class 'numpy.ndarray'>



'''
logspace()
----------
Syntax --> logspace(<Start_Num>, <End_Num>, <Num_of_Parts>)

Similar to 'linspace()' but 'Start_Num' and 'End_Num' will be considered as 'logN to base 10', see example below,
eg: logspace(0, 5, 6) --> 0 to 5 will not be divided into 6 parts, instead log0 to log5 will be divided into 6 parts.

NOTE : log0 means, '10 power of 0'. log5 means '10 power of 5'

NOTE : like linspace(), default value of 'Num_of_Parts' is 50.

NOTE: the result will always be float values.
'''
a = logspace(0,5,3)     # log0 to log5 will be divided into 2 parts.
print(a)                # Output --> [1.00000000e+00 3.16227766e+02 1.00000000e+05]
a = logspace(0,5)       # log0 to log5 will be divided into 50 parts.
print(type(a))          # Output --> <class 'numpy.ndarray'>



'''
arange()
--------
This is same as 'range()' no difference.
'''
a = arange(0,5)
print(a)                # Output --> [0 1 2 3 4]
a = arange(0,5,2)
print(a)                # Output --> [0 2 4]

print(type(a))          # Output --> <class 'numpy.ndarray'>


'''
zeros()
--------
generates ndarray of 0's 
'''
a = zeros(5)
print(a)                # Output --> [0. 0. 0. 0. 0.]
a = zeros(5,int)
print(a)                # Output --> [0 0 0 0 0]
print(type(a))          # Output --> <class 'numpy.ndarray'>



'''
ones()
------
generates ndarray of 1's 
'''
a = ones(5)
print(a)                # Output --> [1. 1. 1. 1. 1.]
a = ones(5,int)
print(a)                # Output --> [1 1 1 1 1]
print(type(a))          # Output --> <class 'numpy.ndarray'>


