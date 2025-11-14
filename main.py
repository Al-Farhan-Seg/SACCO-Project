from member_module import *
from account_module import *
from saving_module import *
from staff_module import *
from loan_module import *
from withdraw_module import *

#----------MEMBER instance--------------
m1 = Premium_Member("MB-001", "Farhan", "Segujja", "Male", "0754882329", "Matugga", "C.E.O")
m1.set_email()
print(m1.get_email())

#------------ACCOUNT instance plus COMPOSITION in attributes---------
acc1 = Account("4300-1278", m1, "Savings")
print(m1.Deposit(200000, acc1))
print(f"ACCOUNT_BALANCE after using MEMBER CLASS method: {acc1.Get_Balance()}")


#-------------SAVING instance plus COMPOSITION in methods------------
s = Saving(20000, "February", 2020)
print()
print(s.Record_Deposit(acc1))
print(f"ACCOUNT_BALANCE after using SAVING CLASS method: {acc1.Get_Balance()}")


#-------------STAFF instance----------------------------
print()
f1 = Fulltime_Staff("S-001", "Farhan", "Segujja", "Male", "Manager", 20)
print(f1.set_salary(20000))
print(f1.compute_Salary())

f2 = PartTime_Staff("S-002", "Lwanga", "Najib", "Male", "Treasurer", 5000)
print(f2.compute_Salary(10))

#-------------LOAN instance--------------
print()
loan1 = Loan("L-0115", m1, 10000, 20)
loan1.set_payment_amount()
loan1.Approve_Loan()

#------------LOAN PAYMENT instance plus composition in attributes
p1 = Loan_Payment(loan1, "P-12768", 2000, "May", 2025)
print(p1.Record_Payment())


#------------WITHDRAW instance plus composition in attributes
w1 = Withdraw("W-001", acc1)
w1.Initiate_Withdraw()
print(f"ACCOUNT_BALANCE after using WITHDRAW CLASS method: {acc1.Get_Balance()}")
