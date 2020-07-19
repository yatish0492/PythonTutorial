'''
Print Prime Numbers

Prime Number --> A number which is divisible by itself and 1 only.
'''

input = int(input("Enter the number to check for prime number :"))

for a in range(2,input) :
    if input % a == 0:
        print(str(input) + " is a not a prime number")
        break
else :
    print(str(input) + " is a prime number")