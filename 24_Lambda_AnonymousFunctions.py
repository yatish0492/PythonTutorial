'''
Lambda or Anonymous functions
-----------------------------
Same as lambdas in Java only diff is instead of '->', we use ':'. and the function should be preceeded by keyword 'lamnbda'

'''


additionLambda = lambda a,b : a + b

print(additionLambda(2,3))


'''evenOddLambda = lambda a :               # Error. Cannot define lambda's in multiple lines.
                    if a % 2 == 0 :
                        return True
                    else :
                        return False'''

evenOddLambda1 = lambda a : a % 2 == 0

print(evenOddLambda1(5))
