'''
Fibonacci Series
----------------
0 1 1 2 3 5 8 13 ....
'''

def Fibonacci(n) :
    a = 0
    b = 1
    print(a)
    print(b)

    for i in range(2,n) :       # iterating from 2 as we have already printed 0 and 1
        print(a + b)
        c = b
        b = a + b
        a = c


Fibonacci(10)       # Output --> 0 1 1 2 3 5 8 13 21 34

