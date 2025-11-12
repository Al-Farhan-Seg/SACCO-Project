class Account:

    def __init__(self, account_No, member_ID, account_type):
        self.account_No = account_No
        self.account_type = account_type
        self.member_ID = member_ID
        self.__balance = 0
        

    def Credit(self, amount):
        if amount <= 0:
            return f"Deposit amount has to be greater than 0"
        else:
            self.__balance += amount
            return f"Your SACCO {self.account_type} account Acc_No. {self.account_No[0:4]}-XXXX has been credited by {amount}......"

    def Debit(self, amount):
        if amount <= 0:
            return "Withdraw amount has to be greater than 0"
        elif amount > self.__balance:
            return "You have Insufficient funds."
        else:
            self.__balance -= amount
            return f"Your SACCO {self.account_type} account Acc_No. {self.account_No[0:4]}-XXXX has been debited by {amount}......"

    
    def Get_Balance(self):
        return self.__balance 
    
