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
from constants import (
    FULL_TIME_PRESENT, PART_TIME_PRESENT, ABSENT
)

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
        is_present, present_status = self.employee_attendance()

        # calling function to calculate daily wage if employee is present.
        if is_present:
            self.calculate_daily_wage(present_status)

    def employee_attendance(self):
        """
        Description:
            This function will check if employee is present or absent and present status
            of employee i.e. whether employe is full time present/ part time present/ absent.
        Return:
            Function will return boolean value. If employee is present, function will 
            return True else it will return false and present status of employee i.e.
            whether employe is full time present/ part time present/ absent.
        """
        is_present = False
        present_status = ABSENT
        emp_check = random.randint(0,2)
        if emp_check == 0:
            is_present = True
            present_status = FULL_TIME_PRESENT
            print("Employee is full time present")
        elif emp_check == 1:
            is_present = True
            present_status = PART_TIME_PRESENT
            print("Employee is part time present")
        else:
            print("Employee is absent")
        return is_present, present_status
    
    def calculate_daily_wage(self, present_status):
        """
        Description:
            This function will calculate daily wages for employee.
        Parameter:
            Present status of employee i.e. whether employe is full time
            present/ part time present/ absent.
        """
        wage_per_hr = 20
        day_hrs = 8
        if present_status == PART_TIME_PRESENT:
            day_hrs = 4
        daily_wages = wage_per_hr*day_hrs
        print(f"Daily wage for employee are {daily_wages}")


# creating object of a class
employee_object = Employee()
employee_object.employee_wage_computation()
