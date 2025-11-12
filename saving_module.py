from account_module import *
class Saving:

    IDs = []

    def ID_gen(self):
        import random
        while True:
            ID = random.randint(100000, 999999)
            if ID not in Saving.IDs:
                Saving.IDs.append(ID)
                False
                return f"TXN-{ID}"
            else:
                continue

    def __init__(self, amount, month, year, date): #removed ACCOUNT_NO and auto-generated DEPOSIT_ID
        self.deposit_ID = self.ID_gen()
        #self.account_No = account_No
        self.amount = amount
        self.month = month
        self.year = year
        self.date = date

    # Composition application............
    def __Update_Balance(self, account_obj):
        account_obj._Account__balance += self.amount
       
    def Record_Deposit(self, account_obj):
        self.__Update_Balance(account_obj)

        return f"""******Payment Received*****
              
Deposit ID: {self.deposit_ID}
Acc_No: {account_obj.account_No[0:4]}-XXXX
Amount: {self.amount}
Date of payment: {self.date}
for: {self.month}-{self.year}"""





#------TESTING--------------
s = Saving(20000, "February", 2020, "Date")
print(s.deposit_ID)

acc1 = Account("4070-4300", "MB-001", "Ordinary Savings")
print(s.Record_Deposit(acc1))
print(acc1._Account__balance)