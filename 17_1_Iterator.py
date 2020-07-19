'''

Iterator
--------
    Same as in java but it doesn't support 'hasNext()' method in python.

    like 'next()' in java, in python we have '__next__()'. since it doesn't have something like 'hasNext()', when we reach
    end of the list then '__next__()' will throw an exception. that is how we find that we have reached the end. I
    personally feel that it is not good. Otherwise we can use a while loop and iterate only for the length of the list.

'''

nums = [7,8,9,10]

it = iter(nums)

print(it.__next__())
print(it.__next__())
print(next(it))         # we can also use 'next(it)' instead of 'it.__next__()'
print(it.__next__())
#print(it.__next__())   # Gives exception by calling next after last  element of list.


# Using 'while' loop to stop after the reaching end of elements.
it1 = iter(nums)

i = 0
while(i<4) :
    print(it1.__next__())
    i += 1