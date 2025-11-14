from datetime import datetime
class Loan:

    def __init__(self, loan_ID, member, loan_amount, payment_period):
        self.loan_ID = loan_ID
        self.member = member
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
Loan Amount: {self.loan_amount}
Loan Applicant: {self.member.first_name} {self.member.last_name}
Membership No: {self.member.member_ID}
Applicant's Contact: {self.member.contact}
Payment Plan: 
            UGX. {self.get_payment_amount()} monthly for {self.payment_period} months\n""")


class Loan_Payment():
    def __init__(self, loan, payment_ID, amount, for_month, for_year):
        self.loan = loan
        self.payment_ID = payment_ID
        self.amount = amount
        self.for_month = for_month
        self.for_year = for_year
        self.date = datetime.now().strftime("%A/%d/%m/%Y, %H:%M:%S")


    def Record_Payment(self):
        self.loan.loan_amount -= self.amount
        print("LOAN PAYMENT RECEIVED".center(50, "."))

        return f""" ------------------------------------------------
|             Payment ID: {self.payment_ID}
| Amount: UGX.{self.amount}
| Paid by: {self.loan.member.first_name} {self.loan.member.last_name} ({self.loan.member.member_ID})
| For: '{self.for_month}-{self.for_year}'
| Date: {self.date}
| Outstanding Loan Amount: UGX.{self.loan.loan_amount}
 ------------------------------------------------"""
        


    