class Student:
    # class variable (static)
    school = 'Techno'

    # constructor with instance variables
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

        # instance method may include getters and setters
    def avg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    # class method (uses a decorator)
    @classmethod
    def getSchool(cls):
        return cls.school

    # static method
    @staticmethod
    def info():
        print('this is a Student class.. in abc module')


s1 = Student(34, 67, 32)
s2 = Student(89, 32, 12)

print(s1.avg())
print(s2.avg())
print(Student.getSchool())
Student.info()
