class Dad:
    def method_dad(self):
        print("This is a part of dad...")

class Mom:
    def method_mom(self):
        print("This is a part of mom...")

class Child(Dad, Mom):
    def method_child(self):
        print("This is a part of child...")

child = Child()
child.method_child()
child.method_dad()
child.method_mom()