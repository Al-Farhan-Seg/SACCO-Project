from datetime import datetime
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

    def __init__(self, amount, for_month, for_year): #removed 'ACCOUNT_NO' and auto-generated DEPOSIT_ID and also removed 'date'
        self.deposit_ID = self.ID_gen()
        self.amount = amount
        self.for_month = for_month
        self.for_year = for_year
        self.date = datetime.now().strftime("%d-%m-%Y")

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
for: {self.for_month}-{self.for_year}"""
