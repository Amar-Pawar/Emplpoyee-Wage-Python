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
            This is a main function.
        """

        print("Welcome To Employee Wage Computation Program")

        # calling function to check employee attendance
        self.employee_attendance()

    def employee_attendance(self):
        """
        Description:
            This function will check if employee is present or absent.
        """
        is_present = 0
        emp_check = random.randint(0,1)
        if emp_check == is_present:
            print("Employee is present")
        else:
            print("Employee is absent")

# creating object of a class
employee_object = Employee()
employee_object.employee_wage_computation()
