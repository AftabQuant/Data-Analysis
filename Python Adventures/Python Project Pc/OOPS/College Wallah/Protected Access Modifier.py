class Professor:
    def __init__(self, name, email_id, phone_no):
        self._name = name # "_" means protected
        self.email_id = email_id
        self.phone_no = phone_no
    def print(self):
        print(self._name, self.email_id, self.phone_no)

kalyan = Professor("Kalyan Maji", "Kalyan@gmail.com", 254634635)
kalyan.print()
print(kalyan._name)