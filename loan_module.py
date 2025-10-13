# from account_module import Account
# class Loan(Account):

class Loan:

    def __init__(self, loan_ID, member_ID, loan_amount, payment_period):
        self.loan_ID = loan_ID
        self.member_ID = member_ID
        self.loan_amount = loan_amount
        self.payment_period = payment_period
        self.__payment_amount = 0


    def Approve_Loan(self):
        print(f"""******Loan Approved******

Loan ID: {self.loan_ID}
Member Id: {self.member_ID}
Loan Amount: {self.loan_amount}
Payment Plan: 
            UGX. {self.get_payment_amount()} monthly for {self.payment_period} months""")

    def Record_Payment(self):
        print(f"""Loan Payment Received
Amount received: *Some_Figure_Here*
Outstanding Loan Amount: {self.loan_amount} - *Some_Figure_Here* """)
        
    def set_payment_amount(self):
        self.__payment_amount = self.loan_amount // self.payment_period

    def get_payment_amount(self):
        return self.__payment_amount
    