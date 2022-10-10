print("getters and Setters - Change ROll number of jessa from 10 to 25 ")
class Student:
    def __init__(self, name, roll_no, age):
        self.name = name #Private member
        self.__roll_no = roll_no
        self.__age = age

    def show(self):
        print('Student Details:', self.name, self.__roll_no)
    def get_roll_no(self):
        return self.__roll_no
    def set_roll_no(self, number):
        if number > 50:
            number=int(input())
            print('Invalid roll no. roll number set to default:25')
        else:
            self.__roll_no = number

jessa = Student('Jessa', 10, 15)
jessa.show()
jessa.set_roll_no(120)


jessa.set_roll_no(25)
jessa.show()