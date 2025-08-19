# test_employee.py

from employee import Employee

def test_give_default_raise():
    """Test the default raise amount of 5000"""
    emp = Employee('John', 'Doe', 50000)  # Create a new employee
    emp.give_raise()  # Use default raise
    assert emp.annual_salary == 55000  # Check result

def test_give_custom_raise():
    """Test a custom raise amount"""
    emp = Employee('Jane', 'Smith', 60000)
    emp.give_raise(10000)  # Custom raise
    assert emp.annual_salary == 70000
