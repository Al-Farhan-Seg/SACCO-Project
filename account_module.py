class Account:

    def __init__(self, account_No, member_ID, account_type):
        self.account_No = account_No
        self.account_type = account_type
        self.member_ID = member_ID
        self.__balance = 0
        

    def Credit(self):
        print(f"""Your SACCO {self.account_type} account Acc_No. {self.account_No[0:4]}-XXXX has been credited......""")
        # return f"""Your SACCO {self.account_type} account Acc_No. {self.account_No[0:4]}-XXXX has been credited......"""

    def Debit(self):
        print(f"""Your SACCO {self.account_type} account Acc_No. {self.account_No[0:4]}-XXXX has been debited......""")
        # return f"""Your SACCO {self.account_type} account Acc_No. {self.account_No[0:4]}-XXXX has been debited......"""
    
    def Get_Balance(self):
        return self.__balance 
    
