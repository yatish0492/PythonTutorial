'''
Variables in Python
-------------------
List is identified by [ ].
List is Mutable.
List is heterogeneous.
'''

# List is Heterogeneous
a = [1,2,"yatish",25.3]
print(a)                    # Output --> [1, 2, 'yatish', 25.3]

# Like String it is negative indexed from end
a = [1,2,"yatish",25.3]
print(a[-1])                 # Output --> 25.3

# Like String we can use range in index
a = [1,2,"yatish",25.3]
print(a[1:3])               # Output --> [2, 'yatish']
print(a[:3])                # Output --> [1, 2, 'yatish']
print(a[2:])                # Output --> ['yatish', 25.3]

# List is Mutable unlike string
a = [1,2,"yatish",25.3]
a[1] = "ashok"                         # Replace "yatish" with "ashok". replaced 1 with 1
print(a)
a = [1,2,"yatish",25.3]
a[1:3] = ["ashok","ramya"]             # Replace 2,"yatish" with "ashok","ramya". replaced 2 with 2
print(a)
a = [1,2,"yatish",25.3]
a[1:3] = ["ashok","ramya","gagan"]    # Replace 2,"yatish" with "ashok","ramya","gagan". replaced 2 with 3
print(a)
a = [1,2,"yatish",25.3]
a[1:3] = ["ashok"]                    # Replace 2,"yatish" with "ashok". replaced 2 with 1
print(a)


# Multi dimension List
a = [[1,2,3],[4,5,6]]
print(a[1][1])


# adding a new element to List. append() will add element at the last
a = [1,2,"yatish",25.3]
a.append(4)                         # Output --> [1, 2, 'yatish', 25.3, 4]
print(a)
a = [1,2,"yatish",25.3]
a.append([4,5])                     # Output --> [1, 2, 'yatish', 25.3, [4, 5]]. It will not add 4 and 5 seperately
print(a)                            # to list. it actually adds one element only which will be list of [4,5]


# adding a new element to List at specified index. insert(index,element)
a = [1,2,"yatish",25.3]
a.insert(2,"ashok")                 # Output --> [1, 2, 'ashok', 'yatish', 25.3]. inserted "ashok" at index 2 and
print(a)                            # pushed other elements by 1 index.

# adding a list of elements as individual elements to list.
a = [1,2,"yatish",25.3]             # Output --> [1, 2, 'yatish', 25.3, 4, 5]. instead of adding single element [4,5]
a.extend([4,5])                     # to list. it added individual elements 4 and 5
print(a)

# remove element. pop()
a = [1,2,"yatish",25.3]
a.pop()                             # Remove last element
print(a)
a = [1,2,"yatish",25.3]
a.pop(1)                            # Remove element at index 1
print(a)

# remove elements using range. del
a = [1,2,"yatish",25.3]
del a[1:3]                          # Output --> [1, 25.3]. remove elements in range of [1:3]
print(a)

# clear the list
a = [1,2,"yatish",25.3]
a.clear()
print(a)

# min(list). similarly max(list), sum(list)
a = [1,2,25.3]
print(min(a))                       # Output --> 1.
a = [1,2,"yatish",25.3]
#min(a)                             # Output --> TypeError: '<' not supported between instances of 'str' and 'int'

# sort()
a = [5,4,3,2,1]
a.sort()
print(a)                            # output --> [1, 2, 3, 4, 5]









