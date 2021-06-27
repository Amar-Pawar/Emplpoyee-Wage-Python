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
    FULL_TIME_PRESENT, PART_TIME_PRESENT, ABSENT, MONTHLY_DAYS,
    MAX_WORKING_HRS
)

class Employee:
    # creating a contsructor
    def __init__(self):
        pass

    def employee_wage_computation(self, wage_type):
        """
        Description:
            This is a main function. It will call other methods.
        Parameter:
            Takes input wage type - monthly / daily
        """

        print("Welcome To Employee Wage Computation Program")

        if wage_type.lower() == "daily":
            # calling function to check employee attendance
            present_status = self.employee_attendance()

            # calling function to calculate daily wage.
            daily_wage = self.calculate_daily_wage(present_status)        

        if wage_type.lower() == "monthly":
            # calling function to calculaye monthly wage.
            monthly_wages = self.calculate_monthly_wage()

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
        present_status = ABSENT
        emp_check = random.randint(0, 2)
        employee_attendance_check_dict = {
            0: FULL_TIME_PRESENT,
            1: PART_TIME_PRESENT,
            2: ABSENT
        }
        present_status = employee_attendance_check_dict[emp_check]
        if present_status == FULL_TIME_PRESENT:
            print("Employee is full time present")

        if present_status == PART_TIME_PRESENT:
            print("Employee is part time present")

        if present_status == ABSENT:
            print("Employee is absent")

        return present_status
    
    def calculate_daily_wage(self, present_status):
        """
        Description:
            This function will calculate daily wages for employee.
        Parameter:
            Present status of employee i.e. whether employe is full time
            present/ part time present/ absent.
        Return:
            This function will return daily wages.
        """
        if present_status == ABSENT:
            daily_wages = 0
            return daily_wages
        wage_per_hr = 20
        day_hrs = 8
        if present_status == PART_TIME_PRESENT:
            day_hrs = 4
        daily_wages = wage_per_hr*day_hrs
        print(f"Daily wage for employee are {daily_wages}")
        return daily_wages

    def calculate_monthly_wage(self):
        """
        Description:
            This function will calculate monthly wages for employee till condition of max working days
            or max working hours is reached.
        Return:
            This function will return monthly wages.
        """
        monthly_wages = 0
        total_working_hrs = 0
        for days in range(0, MONTHLY_DAYS):
            print("Day- "+ str(days+1))
            present_status = self.employee_attendance()
            daily_wages = self.calculate_daily_wage(present_status)
            working_hrs = self.get_working_hrs(present_status)
            total_working_hrs = total_working_hrs + working_hrs

            monthly_wages += daily_wages
            if total_working_hrs == MAX_WORKING_HRS:
                print(f"Max working hours reached {total_working_hrs}")
                break
        print("Total Working Hours: ", total_working_hrs)
        print("Monthly wages ", monthly_wages)
        return monthly_wages
    
    def get_working_hrs(self, present_status):
        """
        Description:
            This function will return working hrs based on present status
        Parameters:
            It takes present_status of employee
        Return:
            This function will return working hrs.
        """
        working_hrs = 0
        if present_status == FULL_TIME_PRESENT:
            working_hrs = 8
        if present_status == PART_TIME_PRESENT:
            working_hrs = 4
        return working_hrs


# creating object of a class
employee_object = Employee()
wage_type = input("Enter wage type monthly/daily : ")
employee_object.employee_wage_computation(wage_type)
