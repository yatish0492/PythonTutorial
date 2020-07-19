'''

Exception Handling
------------------
    In python we use 'try','except' and 'finally' to handle exceptions

'''



try :

    a = 1/0         # this will trigger 'ZeroDivisionError'
    #b = abc     # this will trigger 'NameError' as 'abc is not defined

except ZeroDivisionError as e:      # we use 'as' keyword for variable name 'e'
    print("Zero division exception occurred" + e)
except Exception as e :
    print("Exception occured" + e)

finally:
    print("Finally block executed")





