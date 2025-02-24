class Python:
    def print(self):
        print("I am from python class...")

class Java:
    def print(self):
        print("I am from java class...")

def language(x):
    return x.print()

python = Python()
language(python)

java = Java()
language(java)