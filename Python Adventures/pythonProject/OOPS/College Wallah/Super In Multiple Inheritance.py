class Dad:
    def print(self):
        print("This is a part of dad...")

class Mom:
    def print(self):
        print("This is a part of mom...")

class Child(Dad, Mom):
    def print(self):
        super().print() # MRO -> Method Revolution Order || Print (print func) of Dad
        print("This is a part of child...")

child = Child()
child.print()