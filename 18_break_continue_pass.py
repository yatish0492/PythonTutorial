'''
break and continue is same as that of java.

'pass' is the new one available in python

pass
----
in python we cannot simply leave empty body like {} for a while,for,if,else,elif, function body, class body etc. python give a error.
 If we need to leave the body of these as empty then we have to mention 'pass' mandatory.


NOTE: 'pass' is equivalent of {}

'''


for x in range(10) :
    pass                    # as we can see we don't want to do anything here. we need to leave it empty, so
                            # we have to mention 'pass' otherwise python will give 'error'

if(True) :
    pass                    # mentioning empty body - {}

