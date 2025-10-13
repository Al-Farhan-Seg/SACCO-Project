from member_module import Member

class Account(Member):

    def __init__(self, account_No, member_ID, first_name, last_name, gender, contact, account_type):
        super().__init__(member_ID, first_name , last_name, gender, contact)
        #self.member_ID = member_ID
        self.account_No = account_No
        self.account_type = account_type
        self.__balance = 0
        

    def Credit(self):
        print(f"""Dear {self.first_name} {self.last_name},
    Your SACCO {self.account_type} account Acc_No. {self.account_No[0:4]}-XXXX has been credited......""")
        # return f"""Dear {self.first_name} {self.last_name},
    #Your SACCO {self.account_type} account Acc_No. {self.account_No[0:4]}-XXXX has been credited......"""

    def Debit(self):
        print(f"""Dear {self.first_name} {self.last_name},
    Your SACCO {self.account_type} account Acc_No. {self.account_No[0:4]}-XXXX has been debited......""")
        # return f"""Dear {self.first_name} {self.last_name},
    #Your SACCO {self.account_type} account Acc_No. {self.account_No[0:4]}-XXXX has been debited......"""
    
    def Get_Balance(self):
        return self.__balance 
    
