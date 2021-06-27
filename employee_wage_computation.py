'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-06-27
@Last Modified by: Amar Pawar
@Last Modified time: 2021-06-27
@Title : Employee Wage Computation
/**********************************************************************************
'''
import random

class Employee:
    # creating a contsructor
    def __init__(self):
        pass

    def employee_wage_computation(self):
        """
        Description:
            This is a main function. It will call other methods.
        """

        print("Welcome To Employee Wage Computation Program")

        # calling function to check employee attendance
        is_present = self.employee_attendance()

        # calling function to calculate daily wage if employee is present.
        if is_present:
            self.calculate_daily_wage()

    def employee_attendance(self):
        """
        Description:
            This function will check if employee is present or absent.
        Return:
            Function will return boolean value. If employee is present, function will 
            return True else it will return false.
        """
        is_present = False
        emp_check = random.randint(0,1)
        if emp_check == 0:
            is_present = True
            print("Employee is present")
        else:
            print("Employee is absent")
        return is_present
    
    def calculate_daily_wage(self):
        """
        Description:
            This function will calculate daily wages for employee.
        """
        wage_per_hr = 20
        full_day_hrs = 8
        daily_wages = wage_per_hr*full_day_hrs
        print(f"Daily wage fo employee are {daily_wages}")


# creating object of a class
employee_object = Employee()
employee_object.employee_wage_computation()
