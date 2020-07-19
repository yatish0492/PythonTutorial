'''

Multi Threading
---------------
    It is same as java.
        We extend 'Thread' class
        We implement 'run' method
        We will call 'start()' on the object to start

    It also supports 'join()'
'''

from time import sleep
from threading import *

class HelloThread(Thread) :     # extending 'Thread' class
    def run(self):              # implementing 'run()' method
        for i in range(20) :
            print("Hello")
            sleep(1)



class HiThread(Thread) :
    def run(self):
        for i in range(3) :
            print("Hi")
            sleep(1)




t1 = HelloThread()
t2 = HiThread()


t1.start()      # starting thread
t2.start()


t1.join()   # This block the execution point here itself until 't1' thread is completed. like how while debugging
            # until we release the control to next step. So already started thread 't2' will still run it doesn't block
            # any other threads which are running. So basically it pauses the 'Main' thread until 't1' thread is done.
t2.join()   # This block the execution point here itself until 't1' thread is completed.

print("Done")