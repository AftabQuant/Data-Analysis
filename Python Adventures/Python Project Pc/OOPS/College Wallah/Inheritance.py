class Animal:
    def makesound(self):
        print("Animal makes a sound...")

class Dog(Animal):
    def bark(self):
        print("Dog barks...")

class Cat(Dog):
    def meow(self):
        print("Cat meows...")

cat = Cat()
cat.meow()
cat.bark()
cat.makesound()