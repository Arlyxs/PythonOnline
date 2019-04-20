class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    # *1
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)

        return s3


    # *3
    def __gt__(self, other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False


    # *4
    def __str__(self):
        return self.m1, self.m2


s1 = Student(58, 69)
s2 = Student(60, 65)

# *2
s3 = s1 + s2
print(s3.m2)

if s1 > s2:
    print('s1 wins')
else:
    print('s2 wins')


print(s1.__str__())

''' *1 to overload the built in method of add so that s1 and s2 may be added we must create our own method for __add__   

*2 when it is added our method overloads the built in method

*3 this is our comparator overload function 

*4 overides the default string method and returns values that we define
'''