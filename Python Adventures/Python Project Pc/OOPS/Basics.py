# Basic : class & object
class Student:
    x = None
obj = Student()
obj.x = 6
print(obj.x)

class Student:
    name = None
    age = None
    marks = None
    def print(self):
        print(self.name)
        print(self.age)
        print(self.marks)

obj = Student()
obj.name = "Aftab"
obj.age = 20
obj.marks = 95.9
obj.print()

# Constructor And Class And Object
class Employee:
    id = None
    name = None
    salary = None
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary
    def display(self):
        print(self.id, " ", self.name, " ", self.salary)
obj = Employee(20002, "Aftab", 50000)
obj.display()