# superclass
class A:
    # constructor
    def __init__(self):
        print('in A init')

    def feature1(self):
        print('feature 1 A works')

# sub-class without inheritance
class B:
    # constructor
    def __init__(self):
        print('in B init')

   
    def feature1(self):
        print('feature 1 B works')


    def feature2(self):
        print('feature 2 works')


''' sub-class with inheritance calls superclass constructor and inherits methods '''

class C(B,A):
   # constructor sub-class with inheritance
    def __init__(self):
        ''' super will call constructor from left to right as defined in the class definition '''
        super().__init__()
        print('in C init')

    # *2
    def feat(self):
        super().feature2()


obj1 = C()

# *1
obj1.feature1()
obj1.feature2()

obj1.feat()


''' *1 method resolution order will call the method from the super class based on the order in the class definition ie B first.

*2 the super() method can be used to call other methods '''