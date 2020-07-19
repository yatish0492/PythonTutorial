'''

Duck Typing
-----------
    We can pass/assign any class obj to a variable as we don't specify the type of variable any class object can be
    assigned to it.

'''


class StartCar:
    def start(self, someCar):   # We are passing 'Cruze' and 'Ritz' class objects to same parameter 'someCar'
        print("Starting car " + someCar.name)


class Cruze:
    name = "Cruze"

class Ritz:
    name = "Ritz"


cruzeObj = Cruze()
ritzObj = Ritz()
startCarObj = StartCar()


startCarObj.start(cruzeObj)     # We are passing 'Cruze' class object
startCarObj.start(ritzObj)      # We are passing 'Ritz' class object to the same method