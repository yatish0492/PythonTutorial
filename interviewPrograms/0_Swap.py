'''
Swapping 2 variables
'''


a = 10
b = 20


# Using temp variable
temp = a
a = b
b = temp

# Using summation
a = a + b
b = a - b
a = a - b

# Using xor
a = a ^ b
b = a ^ b
a = a ^ b


# *******************************
# Using Rot_Two()
# ??????????????????????????????????????????????????????????????? - Need to check how this rot works and is it efficient.
a,b = b,a

