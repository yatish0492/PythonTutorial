'''
Factorial
---------
input -> 5
Factorial --> 5*4*3*2*1
'''

def Factorial(n) :
    if n == 1 :
        return n;
    return n * Factorial(n-1)

result = Factorial(5)

print(result)           # Output --> 120