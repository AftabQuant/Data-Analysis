class Students:
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age
    def display(self):
        print(f"Name is : {self.Name}, And Age Is : {self.Age}")
    def greet(self):
        print("Hello, ", self.Name)

obj = Students("Aftab", 20)
obj.display()
obj.greet()

obj = Students("Ariful", 16)
obj.display()
obj.greet()