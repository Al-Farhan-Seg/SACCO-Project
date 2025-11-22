from time import *

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

        return f"""NEW MEMBER REGISTERED......
Member ID: {self.member_ID}
Name: {self.first_name} {self.last_name}
Contact: {self.contact}
Gender: {self.gender}
Address: {self.address}"""
    
    # ---------An application of COMPOSITION
    def Deposit(self, amount, account_obj):
        print(f"Member {self.member_ID} has initiated a deposit.....")
        sleep(3)
        if amount < 1:
            return "Deposit amount MUST be greater than ZERO(0)"
        if self.member_ID != account_obj.member.member_ID:
            return f"The account provided does not belong to {self.first_name} {self.last_name}"
        
        print(account_obj.Credit(amount))
    
    # ---------An application of COMPOSITION
    def Withdraw(self, amount, account_obj):
        print(f"Member {self.member_ID} has initiated a withdraw.....")
        sleep(3)
        if amount < 1:
            return "Withdraw amount MUST be greater than ZERO(0)"
        if self.member_ID != account_obj.member.member_ID:
            return f"The account provided does not belong to {self.first_name} {self.last_name}"
        print(account_obj.Debit(amount))
    
    def set_email(self):
        self.__email = f"{self.first_name}.".lower() + f"{self.last_name}".lower() + "@gmail.com"
    
    def get_email(self):
        return self.__email
    
class Premium_Member(Member):
    def __init__(self, member_ID, first_name, last_name, gender, contact, address, position):
        super().__init__(member_ID, first_name, last_name, gender, contact, address)
        self.loan_svg_percentage = 0.5
        self.position = position

    def terminate_Member(self, person):
        print(f"The {self.position} ({self.first_name} {self.last_name}) has terminated {person} from the SACCO.")

    def make_policy(self, policy):
        print(f"The {self.position} (Mr./Mrs. {self.first_name}) has approved new policy: {policy}.")


class Ordinary_Member(Member):
    def __init__(self, member_ID, first_name, last_name, gender, contact, address):
        super().__init__(member_ID, first_name, last_name, gender, contact, address)
        self.loan_svg_percentage = 0.1
        self.voting = True # Some members have the RIGHT TO VOTE

    def vote_on_policy(self, decision):
        if self.voting == True:
            print(f"Name: {self.first_name} {self.last_name}")
            print("Voting Rights: ACCEPTED")
            print(f"Decision: {decision}")
        else:
            print(f"Name: {self.first_name} {self.last_name}")
            print("Voting Rights: NOT ALLOWED")
            print(f"Decision: INVALID")


