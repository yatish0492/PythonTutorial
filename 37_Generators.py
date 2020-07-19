'''

 Generators will generate a list of elements. 'yield' key word will add the elements to the list.
'''


def getEvenNumbers():   # this function will return the list of even numbers. we are calling 'yield' for each even
    i = 0               # number in this function.
    while i <= 100:
        yield i
        i = i + 2



evenNumbers = getEvenNumbers()

for each in evenNumbers:
    print(each)

