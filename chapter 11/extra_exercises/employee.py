# Module: employee.py

class Employee:
    """A simple class to represent an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        """
        Initialize the employee's first name, last name, and annual salary.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """
        Increase the employee's salary by the given amount.
        Default raise is 5000 if no amount is provided.
        """
        self.annual_salary += amount
