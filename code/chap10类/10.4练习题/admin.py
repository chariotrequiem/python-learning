# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/26 10:11
class User:
    def __init__(self, first_name, last_name, age):
        """初始化属性first_name和last_name,age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        name = self.first_name + " " + self.last_name
        print("The information of the user is as following: ")
        print("Name: " + name.title())
        print("Age: " + str(self.age))

    def greet_user(self):
        name = self.first_name + " " + self.last_name
        print("\nWelcome to log in, honored " + name.title() + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("\nThe privileges of adminer as following: ")
        for privilege in self.privileges:
            print("-" + privilege)


class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privilege = Privileges()
