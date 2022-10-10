import time
print('Destructor - Create a constructor of Student class and destroy the object after displaying it')
class Student:

    def __init__(self, name):
        print('Inside Constructor')
        self.name = name

    def show(self):
        print('Hello, my name is', self.name)

    def __del__(self):
        print('Object destroyed')

s1 = Student('Emma')
s2 = s1
s1.show()

del s1
time.sleep(5)
print('After sleep')
s2.show()