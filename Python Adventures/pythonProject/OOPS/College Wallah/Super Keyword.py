class Parent:
    def print(self):
        print("I am from parent class...")

class Child(Parent):
    def print(self):
        super().print() # When the method's name is same of parent and child.
        print("I am from child class...")


child = Child()
child.print()
