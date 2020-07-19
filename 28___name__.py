'''
__name__
----------
This is a special variable which will give us the module name.

'''


def printCurrentModule() :
    print(__name__)


import packageY.Substraction as sub


printCurrentModule()            # Output --> __main__. Since we are executing this module. this module will be considered
                                #                      as main module. if we execute 'packageY.Substraction', then that
                                #                      will be considered as the main module.

sub.printCurrentModule()        # Output --> packageY.Substraction


if __name__ == "__main__" :
    print("This module is executed as main function/module")

