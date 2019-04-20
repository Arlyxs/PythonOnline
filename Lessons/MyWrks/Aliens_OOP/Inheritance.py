class A:

    def feature1(self):
        print('feature 1 working')


    def feature2(self):
        print('feature 2 working')

# B inherits class A features
class B(A):

    def feature3(self):
        print('feature 3 works')

    def feature4(self):
        print('feature 4 works')

# class without inheritance
class C:

    def feature5(self):
         print('feature 5 is working')

# inherits from B and C (multiple inheritance)
class D(B, C):

    def feature6(self):
        print('feature 6 works also')

class E(D):

    def feature7(self):
        print('feature 7 is good')


a1 = A()
a2 = A()
b1 = B()
c1 = C()
d1 = D()
e1 = E()

a1.feature1()
b1.feature2()
b1.feature3()
c1.feature5()
d1.feature5()
e1.feature6()




