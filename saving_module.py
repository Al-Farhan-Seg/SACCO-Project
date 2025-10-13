class Saving:

    def __init__(self, deposit_ID, account_No, amount, month, year, date):
        self.deposit_ID = deposit_ID
        self.account_No = account_No
        self.amount = amount
        self.month = month
        self.year = year
        self.date = date


    def Update_Balance(self):
        print("*****Balance Updated*****")
        print("New Balance: 'UNSPECIFIED yet' ")

    def Record_Deposit(self):
        print(f"""******Payment Received*****
              
Deposit ID: {self.deposit_ID}
Acc_No: {self.account_No[0:4]}-XXXX
Amount: {self.amount}
Date of payment: {self.date}
for: {self.month}-{self.year}""")
        # return """ """
    