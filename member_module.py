from account_module import Account

class Member:

    def __init__(self, member_ID, first_name, last_name, gender, contact, address):
        self.member_ID = member_ID
        self.first_name = first_name
        self.last_name = last_name
        self.__email = ""
        self.gender = gender
        self.contact = contact
        self.address = address
        

    
    def Register(self):

        return f"NEW MEMBER REGISTERED......\n{self.member_ID}---{self.first_name} {self.last_name}"

    def Deposit(self, amount):
        print(f"Member {self.member_ID} has initiated a deposit.....")
        # return f"Member {self.member_ID} has initiated a deposit.....\n"
    
    def Withdraw(self, amount):
        print(f"Member {self.member_ID} has initiated a withdraw.....")
        # return f"Member {self.member_ID} has initiated a withdraw.....\n"
    
    def set_email(self):
        self.__email = f"{self.first_name}.{self.last_name}@gmail.com"
    
    def get_email(self):
        return self.__email
    
class Premium_Member(Member):
    def __init__(self, member_ID, first_name, last_name, gender, contact, address, position):
        super().__init__(member_ID, first_name, last_name, gender, contact, address)
        self.loan_svg_percentage = 50
        self.position = position

    def terminate_Member(self, person):
        print(f"The {self.position} ({self.first_name} {self.last_name}) has terminated {person} from the SACCO.")

    def make_policy(self, policy):
        print(f"The {self.position} (Mr./Mrs. {self.first_name}) has approved new policy: {policy}.")


class Ordinary_Member(Member):
    def __init__(self, member_ID, first_name, last_name, gender, contact, address, voting):
        super().__init__(member_ID, first_name, last_name, gender, contact, address)
        self.loan_svg_percentage = 10
        self.voting = True

    def vote_on_policy(self, decision):
        if self.voting == True:
            print(f"Name: {self.first_name} {self.last_name}")
            print("Voting Rights: ACCEPTED")
            print(f"Decision: {decision}")
        else:
            print(f"Name: {self.first_name} {self.last_name}")
            print("Voting Rights: NOT ALLOWED")
            print(f"Decision: INVALID")




