from member_module import Member
from saving_module import Saving
from withdraw_module import Withdraw
from staff_module import Staff
from account_module import Account
from loan_module import Loan

# Instantiating Our FIRST Member object
m1 = Member("MiD_001", "Farhan", "Segujja", "Male", "0754882329", "Matugga")
m1.Register()
m1.Withdraw()
m1.Deposit()

# Instantiating Our SECOND Member object {intended to be used for the STAFF object}
print()
m2 = Member("MiD_002", "Bugembe", "Mahad", 'Male', "0703889536", "Kazo")
m2.Register()
m2.Withdraw()
m2.Deposit()
print(m2.get_email())

# Instantiating Our FIRST Account object
print()
acc1 = Account("4070-4300", m1.member_ID,"Ordinary Savings")
acc1.Credit()
acc1.Debit()
print(f"Account Balance: UGX {acc1.Get_Balance()}")

# Instantiating Our FIRST member of STAFF object {using our SECOND Member instance }
print()
staff_2 = Staff("SiD_002", m2.first_name, m2.last_name, m2.gender, "Manager", m2.member_ID)
staff_2.Approve_loan()
staff_2.Manage_Accounts()
staff_2.Generate_reports()

# Instantiating Our FIRST Withdrawal from the SACCO using {FIRST member instance}
print()
w1 = Withdraw("WiD_001", acc1.account_No, 1000000, "10-Oct-2025")
w1.Check_Balance()
w1.Update_Balance()
w1.Return_Result()

# Instantiating Our FIRST Saving object
print()
sv_1 = Saving("d-iD_001", acc1.account_No, 50000, "February", "2024", "09-09-2025")
sv_1.Update_Balance()
sv_1.Record_Deposit()

# Instantiating Our FIRST Loan object
print()
loan_1 = Loan("LiD_001", acc1.member_ID, 500000, 24)
loan_1.Record_Payment()
loan_1.set_payment_amount()
print(loan_1.get_payment_amount())
loan_1.Approve_Loan()






