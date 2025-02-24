class Test:
    name = "Md Aftab Uddin"
    def greet(self):
        print(f"Hello: {self.name}")

t1 = Test()
t1.greet()

class Addition:
    def add(self,x,y):
        return x+y
a = Addition()
print(a.add(3,5))