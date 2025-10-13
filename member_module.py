class Member:

    def __init__(self, member_ID, first_name, last_name, gender, contact):
        self.member_ID = member_ID
        self.first_name = first_name
        self.last_name = last_name
        self.__email = ""
        self.gender = gender
        self.contact = contact
        #add

    
    def Register(self):
        print(f"NEW MEMBER REGISTERED......\n{self.member_ID}---{self.first_name} {self.last_name}")
        # return f"\nNEW MEMBER REGISTERED......\n{self.member_ID}---{self.first_name} {self.last_name}"

    def Deposit(self):
        print(f"Member {self.member_ID} has initiated a deposit.....")
        # return f"Member {self.member_ID} has initiated a deposit.....\n"
    
    def Withdraw(self):
        print(f"Member {self.member_ID} has initiated a withdraw.....")
        # return f"Member {self.member_ID} has initiated a withdraw.....\n"
    
    def set_email(self):
        self.__email = f"{self.first_name}.{self.last_name}@gmail.com"
    
    def get_email(self):
        return self.__email
    
