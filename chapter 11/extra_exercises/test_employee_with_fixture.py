# test_employee_with_fixture.py

import pytest
from employee import Employee

@pytest.fixture
def employee():
    """Fixture: provides a default Employee instance for multiple tests."""
    return Employee('Alice', 'Johnson', 70000)

def test_give_default_raise(employee):
    """Test default raise using fixture"""
    employee.give_raise()
    assert employee.annual_salary == 75000  # 70000 + 5000

def test_give_custom_raise(employee):
    """Test custom raise using fixture"""
    employee.give_raise(15000)
    assert employee.annual_salary == 85000  # 70000 + 15000
