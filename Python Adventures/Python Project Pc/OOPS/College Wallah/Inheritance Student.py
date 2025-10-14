class Professor:
    def __init__(self, name, email_id, phone_no):
        self.name = name
        self.email_id = email_id
        self.phone_no = phone_no
    def print(self):
        print(self.name, self.email_id, self.phone_no)

class OOPS(Professor):
    def start(self):
        print("Class started..")

oops = OOPS("Kalyan Maji", "Kalyan@gmail.com", 254634635)
oops.print()
oops.start()