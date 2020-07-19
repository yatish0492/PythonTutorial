'''
If statement
------------
Syntax --> if <Expression> :
        OR
Syntax --> if(Expression) :

NOTE --> we don't have {} to enclose the body of if condition. python uses indentation, the body of it should be either
         one space or any number of space after the actual indentation of 'if' keyword. standard is 4 spaces. If any
         line is not with the same indentation as that of 1st line after 'if' statement then those lines are not part
         of the 'if' body.


else statement
--------------
Syntax --> else :


elif statement
--------------
Syntax --> elif :

NOTE --> it is not 'elseif' it is 'elif'

'''


if True :                                   # this with syntax --> if <Expression> :
    print("If condition success!!!")        # This is the body of 'if'
    print("1 Not inside if")                # ERROR : IndentationError: unexpected indent. It should be either 'if' body index or at start cannot be in middle anywhere.
print("2 No inside if")                     # This is not inside 'if'


if(False) :                                  # this with syntax --> if(<Expression>) :
    print("inside if")
elif(True) :                                # elif
    print("inside elif")
else :                                      # else
    print("inside else")


