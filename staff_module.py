from member_module import Member
class Staff(Member):

    def __init__(self, staff_ID, first_name, last_name, gender, contact, position, member_ID):
        super().__init__(member_ID, first_name, last_name, gender, contact)
        self.staff_ID = staff_ID
        self.position = position



    def Approve_loan(self):
        print(f"Loan Approved..........\nProcessed by: {self.first_name} {self.last_name}")
        # return f"Loan Approved..........\nProcessed by: {self.first_name} {self.last_name}"

    def Manage_Accounts(self):
        print(f"Access granted......\nStaff Member: {self.first_name} {self.last_name}\nStaff ID: {self.staff_ID}")
        # return f"Access granted......\nStaff Member: {self.first_name} {self.last_name}\nStaff ID: {self.staff_ID}"
    
    def Generate_reports(self):
        print(f"Report generated.......\nGenereted by: {self.first_name} {self.last_name}")
        # return f"Report generated.......\nGenereted by: {self.first_name} {self.last_name}"