class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

    def working(self):
        print('working ')
    def coding(self):
        print('coding')

    # def working():
    #     print('working ')
    # def coding():
    #     print('coding')

class Student(Person):
    def __init__(self, name, phoneNumber, subject, studentID):
        Person.__init__(self, name, phoneNumber)
        # self.name = name
        # self.phoneNumber = phoneNumber
        self.subject = subject
        self.studentID = studentID

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
        print("Info(Subject:{0}, studentID: {1})".format(self.subject, self.studentID))

p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
# print(p.__dict__)
# print(s.__dict__)
p.printInfo()
s.printInfo()
p.working()
s.coding()


