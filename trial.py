mylist= [['name', 'wick'], ['email', 'wick@gmail.com'], ['age', 89]]

print(dict(mylist))

class Account():



    def __init__(self, name='', email='', phone_number='', gender=''):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.gender = gender

    def get_info(self):
        self.name = input("Enter Name here: ")
        self.email = input("Enter email here: ")
        self.phone_number = input("Enter phone_number here: ")
        self.gender = input("Enter gender here: ")

        print(self.name, self.email, self.phone_number, self.gender, sep=" // ")


