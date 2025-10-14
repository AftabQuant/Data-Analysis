import json

class Employee:
    def __init__(self, Name, Id, Salary):
        self.Name = Name
        self.Id = Id
        self.Salary = Salary
    def print_info(self):
        print("Name Is: ", self.Name)
        print("Id Is : ", self.Id)
        print("Salary Is : ", self.Salary)
    def increment_salary(self, increment):
        self.Salary += increment
    def save_in_json(self, FileName):
        my_data = {"Name ": self.Name, "Id " :self.Id, "Salary":self.Salary}
        with open(FileName, "w") as f:
            f.write(json.dumps(my_data, indent=4))

    def load_from_json(self, fileName):
        with open(fileName, "r") as f:
            data = json.loads(f.read())
        print(data)

e1 = Employee("Aftab", 23, 34000)
e1.print_info()
e1.save_in_json("Employee.json")
e1.load_from_json("Employee.json")