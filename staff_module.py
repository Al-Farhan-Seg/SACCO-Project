class Staff:

    def __init__(self, staff_ID, first_name, last_name, gender, position):
        self.staff_ID = staff_ID
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.position = position
        self.salary = 0


    def Approve_loan(self):
        print(f"Loan Approved..........\nProcessed by: {self.first_name} {self.last_name}")
        # return f"Loan Approved..........\nProcessed by: {self.first_name} {self.last_name}"

    def Manage_Accounts(self):
        print(f"Access granted......\nStaff Member: {self.first_name} {self.last_name}\nStaff ID: {self.staff_ID}")
        # return f"Access granted......\nStaff Member: {self.first_name} {self.last_name}\nStaff ID: {self.staff_ID}"
    
    def Generate_reports(self):
        print(f"Report generated.......\nGenereted by: {self.first_name} {self.last_name}")
        # return f"Report generated.......\nGenereted by: {self.first_name} {self.last_name}"

    def compute_Salary(self):
        return self.salary


# Polymorphism on its way here.........
class Fulltime_Staff(Staff):
    def __init__(self, staff_ID, first_name, last_name, gender, position, basic_salary):
        super().__init__(staff_ID, first_name, last_name, gender, position)
        self.basic_salary = basic_salary

    def compute_Salary(self):
        return self.basic_salary
    

class PartTime_Staff(Staff):
    def __init__(self, staff_ID, first_name, last_name, gender, position, rate_per_hour):
        super().__init__(staff_ID, first_name, last_name, gender, position,)
        self.rate_per_hour = rate_per_hour

    def compute_Salary(self, hours_worked):
        return hours_worked * self.rate_per_hour
    