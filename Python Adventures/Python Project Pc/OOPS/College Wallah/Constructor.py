class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    def print(self):
        print(self.name, self.age, self.marks)

s1 = Student("Aftab",20,9.8)
s1.print()
s2 = Student("Ariful",17,7.8)
s2.print()
