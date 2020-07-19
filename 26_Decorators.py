'''
Decorators
----------
It is similar to proxies in java

Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class.
Decorators allow us to wrap another function in order to extend the behavior of wrapped function, without permanently modifying it.
'''

def substraction(a,b) :
    return a - b


# Decorator function
# ------------------
# Below function 'extendedSubstractionNoNegativeDiffference()' returns a function which will check if a < b.
# then it swaps value of a and b so that we don't get negative difference. and then it calls the function passed
# as parameter in the below case it is 'substraction(a,b)'
def extendedSubstractionNoNegativeDiffference(func) :

    def makeAVariableBiggerBeforeCallingSubstraction(a, b) :
        if a < b :
            a,b = b,a
        return func(a,b)

    return makeAVariableBiggerBeforeCallingSubstraction


print(substraction(2,5))                    # Output --> -3.

negativeSaveSubstraction = extendedSubstractionNoNegativeDiffference(substraction)

print(negativeSaveSubstraction(2,5))        # Output --> 3