'''
Arithmetic Operators supported
------------------------------
1) +, -, *, /, %
2) +=, -=, *=, /= (Short hand operators)
3) ==, >=, <=, !=
4) and , or, not

NOTE: && and || is operators doesn't work. Instead we need to use 'and' and 'or'

NOTE: ! can be used like !=  for binary operations but as unary/negating operator it is not supported.
       like 'if(!True)' This will give error. Instead you need to use 'if(not True)'

NOTE: ++,-- unary operators doesn't work.

NOTE: for getting power of a number use '**' as '^' means bitwise operator for XOR in python.


Bitwise Operators supported
---------------------------
1) ~ (Complement)
2) & (AND)
3) | (OR)
4) ^ (XOR)
5) << (Left Shift)
6) >> (Right Shift)

'''

# Unary operator. You can make an number from positive to negative easily.
a = 10
a = -a      # making a value as a negative value.
print(a)                    # Output --> -10
# print(!True)     # Output -->  SyntaxError: invalid syntax. Correct way is 'if(not True)' as shown below.
print(not True)


#Converting numbers from decimal to other formats
print(bin(10))      # Output --> 0b1010. 'bin()' function is used to convert to binary.
print(oct(10))      # Output --> 0o12. 'oct()' function is used to convert to octa.
print(hex(10))      # Output --> 0xa. 'hex()' function is used to convert to hexa.
