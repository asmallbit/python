import unittest
from employee import Employee

class Test_Employee(unittest.TestCase):
    def setUp(self):
        first_name = 'jianwei'
        last_name = 'han'
        salary = 50000
        self.employee = Employee(first_name, last_name, salary)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.salary, 55000)

    def test_give_custom_raise(self):
        self.employee.give_raise(20000)
        self.assertEqual(self.employee.salary, 70000)

unittest.main()