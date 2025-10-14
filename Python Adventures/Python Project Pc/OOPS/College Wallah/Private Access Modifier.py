class Professor:
    def __init__(self, name, email_id, phone_no):
        self.__name = name  # Private variable
        self.email_id = email_id
        self.phone_no = phone_no

    def get_name(self):  # Getter method
        return self.__name

    def print(self):
        print(self.__name, self.email_id, self.phone_no)

kalyan = Professor("Kalyan Maji", "Kalyan@gmail.com", 254634635)
kalyan.print()

# Best practice: Use getter method
print(kalyan.get_name())  # ✅ Recommended approach
