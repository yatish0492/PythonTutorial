'''
Tuples are defined using '()'
Tuples are IMutable unlike List. So they are fast in Iteration
Tuple is also heterogeneous.
'''

a = (1,2,"yatish",25.3)  # Tuple is also heterogeneous

# We can access each element of set by using the indexes including negative and ranges as shown below
print(a)
print(a[0])
print(a[-1])
print(a[:3])
print(a[2:])


# But you cannot change any element in tuple once created because, it is immutable
a[0] = 10;


