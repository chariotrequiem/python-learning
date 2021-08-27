# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/27 10:08
class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_salary(self, raise_salary=5000):
        """年薪增加"""
        self.annual_salary = self.annual_salary + raise_salary
        return self.annual_salary
