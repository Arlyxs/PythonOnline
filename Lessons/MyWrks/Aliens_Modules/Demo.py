# import Calc
# from Calc import *

# c = Calc.add(9, 7)
# print(c)

'''
create a main module then create separate files or
folders to draw sub-modules from.  eg a Demo module, then a
Calc sub-module with add, sub, multiply, divide functions.

in the Demo module import the sub-module eg
from Calc import * - then can use any of the functions add etc
or in Demo import Calc then use Calc.add or Calc.divide etc
'''


def main():
    print('hello')
    print('welcome user')


if __name__ == "__main__":
    main()
# special variable __name__ in PYthon
# print('Demo says: ' + __name__)
'''
prints the starting point of the program filethat you are in.
therefore will print calc print statement first as it is imported first.
to avoid that can insert an if statement to restrict what __name__ recognises
'''
