class Staff:

    def __init__(self, staff_ID, first_name, last_name, gender, position):
        self.staff_ID = staff_ID
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.position = position
        self.__basic_salary = 0


    def Approve_loan(self):

        return f"Loan Approved..........\nProcessed by: {self.first_name} {self.last_name}"

    def Manage_Accounts(self):

        return f"Access granted......\nStaff Member: {self.first_name} {self.last_name}\nStaff ID: {self.staff_ID}"
    
    def Generate_reports(self):

        return f"Report generated.......\nGenereted by: {self.first_name} {self.last_name}"

    def compute_Salary(self):
        return self.__basic_salary


# Polymorphism on its way here.........
class Fulltime_Staff(Staff):
    def __init__(self, staff_ID, first_name, last_name, gender, position, experience):
        super().__init__(staff_ID, first_name, last_name, gender, position)
        self.__basic_salary = 0
        self.experience = experience

    def set_salary(self, amount):
        self.__basic_salary = amount
        return f"Salary for {self.first_name} {self.last_name} successfully set"

    def compute_Salary(self):
        if self.experience > 7:
            bonus = 0.4 * self.__basic_salary
        else:
            bonus = 0.1 * self.__basic_salary
        self.__basic_salary += bonus

        return self.__basic_salary
    

class PartTime_Staff(Staff):
    def __init__(self, staff_ID, first_name, last_name, gender, position, rate_per_hour):
        super().__init__(staff_ID, first_name, last_name, gender, position)
        self.rate_per_hour = rate_per_hour

    def compute_Salary(self, hours_worked):
        return hours_worked * self.rate_per_hour
    
