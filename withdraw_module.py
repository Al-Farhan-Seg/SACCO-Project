class Withdraw:

    def __init__(self, withdraw_ID, account_No, amount, date):
        self.withdraw_ID = withdraw_ID
        self.account_No = account_No
        self.amount = amount
        self.date = date
        

    def Check_Balance(self):
        print(f"Checking balance of Acc_No. {self.account_No}.......")
        

    def Update_Balance(self):
        # find a way of trying to make the account balance ZERO(0)
        print(f"Balance of Acc.No. {self.account_No} has been updated........")
    
    def Return_Result(self):
        print(f"Owner of Acc_No {self.get_account_No()} has succesfully withdrawn from the SACCO......")

    