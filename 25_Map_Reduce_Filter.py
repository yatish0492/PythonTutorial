'''
Map, Reduce and Filter
----------------------
Same as java and spark

NOTE: All Map,Reduce and Filter functions will return a function object so we need to explicitly convert them to list using 'list()'
'''

input = range(10)

'''
filter
------
filter function takes, input lambda function and the list to be processed.
Below filter function will filter out only even numbers.
'''
evenNumbers = filter(lambda a : a%2 == 0, input)

evenNumbers = list(evenNumbers)     # Converting to list from function object.

print(evenNumbers)                  # Output --> [0, 2, 4, 6, 8]


'''
map
---
map function takes, input lambda function and the list to be processed.
Below map function will add '2' to each and element in 'evenNumbers'.
'''

evenNumbersAddedWith2 = map(lambda a : a + 2, evenNumbers)

evenNumbersAddedWith2 = list(evenNumbersAddedWith2)     # Converting to list from function object.

print(evenNumbersAddedWith2)        # Output --> [2, 4, 6, 8, 10]


'''
reduce
------
reduce function takes, input lambda function and the list to be processed.
Below reduce function will return sum of elements in the list 'evenNumbersAddedWith2'

NOTE: 'reduce' function is present in 'functools' library so we need to import it and use it
'''
import functools

FinalSumOfNumbers = functools.reduce(lambda a,b : a+b, evenNumbersAddedWith2)

print(FinalSumOfNumbers)            # Output --> 30
