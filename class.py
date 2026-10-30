class Juth():
    staff = "Staff"
    nysc = "NYSC"

    def __init__(self,name = "", state_code = "", department = ""):
        self.name = name
        self.state_code = state_code
        self.department = department

    def get_info(self):
        details= ["name", "state_code" , "department"]

        self.name = input("Enter your name here: ").upper()
        self.state_code = input("Enter your state_code here: ").upper()
        self.department = input("Enter your department here: ").upper()

    def display_detail(self):
        print("Your name is: {}, state_code: {} and from {} department".format(self.name, self.state_code, self.department))

    def create_user(self):
        pass



class Account():

    def __init__(self, name, email, phone_number, gender ):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.gender = gender


    def create_acct(self):
        pass



worker = Juth()


worker.get_info()
worker.display_detail()