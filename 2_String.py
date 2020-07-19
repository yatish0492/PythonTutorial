'''
Strings in Python
-----------------
String is always considered as array of characters in python
'''


# Strings can be within either "" or ''
print("String in double quotes")
print('String in single quotes')

# Following will print string 10 times
print(10 * 'Printed 10 Times')

# Like java we need to use extra '\' to make things like '\n' not to take effect. it is supported
# in python as well.
print('String with \\n newline character, but new line character will not take effect')

# Raw String
# -----------
# special characters like \n will make the string to break line. in java were using \\n to avoid it.
# in python we can also achieve this by specify 'r' in from of string as shown below so that \n like
# things doesn't take effect.
print(r'String with \n newline character, but new line character will not take effect')

# String is always considered as array of characters so a[1] will give 'a'.
a = "yatish"
print(a[1])

# Negative indexes
# ----------------
# Like how index start from 0 to n from start to end, index also starts from -1 to -n from end to start.
# As per following code, index '5' and '-1' both point to 'h'. index '0' and '-6' points to 'y'
# 'Index out of range' exception happens if we give index outside '-6' to '5'. eg: a[8]
a = "yatish"
print(a[0] + " = " + a[-6])
print(a[5] + " = " + a[-1])

# Range in string (Substring)
# ---------------------------
# we can specify the ranges of index in string to get sub string. eg: a[ StartIndex : EndIndex ]
a = "yatish"
print(a[1:5])    # Output --> 'atis'. startIndex is inclusive but end index is Exclusive
print(a[:5])     # Output --> 'yatis'. if no startIndex then it will consider, '0' as start index
print(a[1:])     # Output --> 'atish'. if no endIndex then it will consider, '6' as end index
print(a[1:500])  # Output --> 'atish'. if end index is out of range also it implicitly considers '6'
                              # doesn't throw index our of range error.
print(a[-500:3]) # Output --> 'yat'. If start index is out of range also it will implicitly considers
                              # the start index '0'


# Strings are immutable like in java
# ----------------------------------
# a[1] = "b"  --> will give error as we cannot modify existing string. it is immutable.
# a[1:3] = "bc" --> will give error.
# a = "Ashok" --> No error as existing string is not changed and new string literal/object "Ashok"
#                 will be created and assigned to 'a' so immutability not broken.
a = "yatish"


# Length function
# ---------------
# len() function is used.
a = "yatish"
print(len(a))







