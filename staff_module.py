class Staff:

    def __init__(self, staff_ID, first_name, last_name, gender, position, member_ID):
        self.staff_ID = staff_ID
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.position = position
        self.member_ID = member_ID


    def Approve_loan(self):
        print(f"Loan Approved..........\nProcessed by: {self.first_name} {self.last_name}")
        # return f"Loan Approved..........\nProcessed by: {self.first_name} {self.last_name}"

    def Manage_Accounts(self):
        print(f"Access granted......\nStaff Member: {self.first_name} {self.last_name}\nStaff ID: {self.staff_ID}")
        # return f"Access granted......\nStaff Member: {self.first_name} {self.last_name}\nStaff ID: {self.staff_ID}"
    
    def Generate_reports(self):
        print(f"Report generated.......\nGenereted by: {self.first_name} {self.last_name}")
        # return f"Report generated.......\nGenereted by: {self.first_name} {self.last_name}"