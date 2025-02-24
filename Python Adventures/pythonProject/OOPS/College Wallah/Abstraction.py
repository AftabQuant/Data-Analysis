from abc import ABC, abstractproperty

class Manager(ABC):
    @abstractproperty
    def class_start(self):
        pass

    @abstractproperty
    def class_end(self):
        pass

class Developar1(Manager):
    def class_start(self):
        print("Kalyan sir will start the class...")
    def class_end(self):
        print("Kalyan sir will end the class...")

class Developar2(Manager):
    def class_start(self):
        print("Sudip sir will start the class...")
    def class_end(self):
        print("Sudip sir will end the class...")
developar1 = Developar1()
developar1.class_start()
developar1.class_end()

developar2 = Developar2()
developar2.class_start()
developar2.class_end()
