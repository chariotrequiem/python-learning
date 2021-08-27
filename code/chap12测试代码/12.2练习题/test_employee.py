# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/27 10:16
import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        """创建一个调查对象，供测试方法使用"""
        self.my_employee = Employee('jack', 'jones', 100000)

    def test_give_default_raise(self):
        """测试默认将年薪增加5000美元"""
        self.my_employee.give_salary()
        self.assertEqual(self.my_employee.annual_salary, 105000)

    def test_give_custom_raise(self):
        """测试年薪可以增加其他增量"""
        self.raise_salary = 8000
        self.my_employee.give_salary(self.raise_salary)
        self.assertEqual(self.my_employee.annual_salary, 108000)


if __name__ == '__main__':
    unittest.main()
