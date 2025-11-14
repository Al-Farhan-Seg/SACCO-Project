from time import *
from datetime import datetime
class Withdraw:

    def __init__(self, withdraw_ID, account):

        self.withdraw_ID = withdraw_ID
        self.account = account
        self.date = datetime.now().strftime("%A/%d/%m/%Y, %H:%M:%S")
        

    def Initiate_Withdraw(self): #renamed from Check_Balance(self)
        print(f"Checking balance of Acc_No. {self.account.account_No}.......")
        sleep(2)
        query = input(f"""You account has {self.account.Get_Balance()} remaining,
Are you sure you want to leave the SACCO and empty your {self.account.account_type} account? (Yes/No)""")

        if query[0].upper() == "Y":
            self.__Update_Balance()
            sleep(2)
            self.__Return_Result()
        else:
            print("The SACCO is happy to have you around🥳🥳🥳")
        

    def __Update_Balance(self):
        # making the account balance ZERO(0)
        self.account._Account__balance = 0
        print(f"Balance of Acc.No. {self.account.account_No} has been SUCCESSFULLY updated to {self.account._Account__balance}")
    
    def __Return_Result(self):
        print(f"{self.account.member.first_name} {self.account.member.last_name} of Acc_No {self.account.account_No} has succesfully withdrawn from the SACCO on '{self.date}' 😭😭😭")
