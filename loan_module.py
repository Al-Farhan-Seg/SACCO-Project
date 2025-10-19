class Loan:

    def __init__(self, loan_ID, member_ID, loan_amount, payment_period):
        self.loan_ID = loan_ID
        self.member_ID = member_ID
        self.loan_amount = loan_amount
        self.payment_period = payment_period
        self.__payment_amount = 0


          
    def set_payment_amount(self):
        self.__payment_amount = self.loan_amount // self.payment_period

    def get_payment_amount(self):
        return self.__payment_amount


    def Approve_Loan(self):
        print(f"""******Loan Approved******

Loan ID: {self.loan_ID}
Member Id: {self.member_ID}
Loan Amount: {self.loan_amount}
Payment Plan: 
            UGX. {self.get_payment_amount()} monthly for {self.payment_period} months\n""")


class Loan_Payment(Loan):
    def __init__(self, loan_ID, member_ID, loan_amount, payment_period, payment_ID, amount, month, year, date):
        super().__init__(loan_ID, member_ID, loan_amount, payment_period)
        self.payment_ID = payment_ID
        self.amount = amount
        self.month = month
        self.year = year
        self.date = date


    def Record_Payment(self):
        self.loan_amount = self.loan_amount - self.amount
        print("LOAN PAYMENT RECEIVED".center(50, "."))

        print(f""" ------------------------------------------------
|             Payment ID: {self.payment_ID}                 |
| Amount received: UGX.{self.amount} from '{self.member_ID}'        |
| for '{self.month}-{self.year}' on Date: {self.date}        |
| Outstanding Loan Amount: UGX.{self.loan_amount}          |
 ------------------------------------------------""")
        

'''l1 = Loan("L001", "M001", 20000000, 23)
l1.set_payment_amount()
l1.get_payment_amount()
l1.Approve_Loan()

l1_p = Loan_Payment(l1.loan_ID, l1.member_ID, l1.loan_amount, l1.payment_period, "PiD001", 120000, "February", "2025", "10-19-2025")
l1_p.Record_Payment()'''
    