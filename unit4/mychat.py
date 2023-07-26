class Person:
    def __init__(self, person_id, name, phone_number):
        self.id = person_id
        self.name = name
        self.phoneNumber = phone_number

    def printInfo(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Phone Number:", self.phoneNumber)
        print()


class Manager(Person):
    def __init__(self, person_id, name, phone_number, skill):
        super().__init__(person_id, name, phone_number)
        self.skill = skill

    def printInfo(self):
        super().printInfo()
        print("Skill:", self.skill)
        print()


class Employee(Person):
    def __init__(self, person_id, name, phone_number, salary):
        super().__init__(person_id, name, phone_number)
        self.salary = salary

    def printInfo(self):
        super().printInfo()
        print("Salary:", self.salary)
        print()


# 예시로 클래스를 사용해봅시다.
if __name__ == "__main__":
    person1 = Person(1, "John", "123-456-7890")
    person1.printInfo()

    manager1 = Manager(2, "Jane", "987-654-3210", "Project Management")
    manager1.printInfo()

    employee1 = Employee(3, "Mike", "555-123-4567", 50000)
    employee1.printInfo()
