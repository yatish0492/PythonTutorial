'''
for Loop

Syntax --> for <VARIABLE> in <CollectionVaraible> :


Doesn't python have a for loop like for(int i =0; i <n; i++) ?
    Unfortunately no. you have to use range to achieve this functionality.

'''

a = ["yatish",3,5.9]

# this is equivalent to foreach loop in java.
for x in a :
    print(x)

# this is equivalent to for(int i =1; i < 10; i++)
for y in range(1,10) :        # Using range in for loop to iterate
    print(y)

# consider i want to achieve for(int i = 20 ; i > 0; i--)
for z in range(20,0,-1) :
    print(z)

# if we give a string to for loop then it iterates over each character.
for x in "yatish" :
    print(x)

'''
for loop with else
------------------
yes!!! we can use else part for a 'for' loop like how we use for 'if'. 

the else part will be called if there is 'break' statement is not executed in 'for' loop. If 'break' statement is 
executed, then control will not goto 'else' part.

'''
a = ["ashok",3,5.9]

for x in a :
    if x == "yatish" :
        print("yes, got yatish")
        break
else :                              # make sure 'else' is at indentation level of 'for'
    print("Didn't Find yatish")







