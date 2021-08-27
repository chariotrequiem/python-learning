# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/26 22:25
"""
下面来编写针对类的测试。很多程序中都会用到类，因此能够证明你的类能够正确地工作会大有裨益。
如果针对类的测试通过了，你就能确信对类所做的改进没有意外地破坏其原有的行为。
"""
# 2.1各种断言方法
"""
Python在unittest.TestCase类中提供了很多断言方法。
前面说过，断言方法检查你认为应该满足的条件是否确实满足。
如果该条件确实满足，你对程序行为的假设就得到了确认，你就可以确信其中没有错误。
如果你认为应该满足的条件实际上并不满足，Python将引发异常。

下面描述了6个常用的断言方法。
使用这些方法可核实返回的值等于或不等于预期的值、返回的值为True或False、返回的值在列表中或不在列表中。
你只能在继承unittest.TestCase的类中使用这些方法。
方法                                用途
assertEqual(a, b)                   核实a == b 
assertNotEqual(a, b)                核实a != b 
assertTrue(x)                       核实x 为True 
assertFalse(x)                      核实x 为False 
assertIn(item , list )              核实item在list中 
assertNotIn(item , list )           核实item不在list中
"""

# 2.2一个要测试的类
"""
类的测试与函数的测试相似——你所做的大部分工作都是测试类中方法的行为，但存在一些不同之处，下面来编写一个类进行测试。
来看一个帮助管理匿名调查的类:
见survey.py
为证明AnonymousSurvey 类能够正确地工作，我们来编写一个使用它的程序：
见language_survey.py
"""

# 2.3测试AnonymousSurvey类
"""
下面来编写一个测试，对AnonymousSurvey类的行为的一个方面进行验证：
如果用户面对调查问题时只提供了一个答案，这个答案也能被妥善地存储。
为此，我们将在这个答案被存储后，使用方法assertIn()来核实它包含在答案列表中：
import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    #针对AnonymousSurvey类的测试

    def test_store_single_response(self):
        #测试单个答案会被妥善的存储
        question = "What language did you first learn to speak? "
        my_survey = AnonymousSurvey(question)
        my_survey.store_responses('English')

        self.assertIn('English', my_survey.responses)

    def test_store_three_response(self):
        #测试三个答案会被妥善的存储
        question = "What language did you first learn to speak? "
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'France', 'Chinese']
        for response in responses:
            my_survey.store_responses(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)


if __name__ == '__main__':
    unittest.main()
"""

# 2.4方法setUp()
"""
在前面的test_survey.py中，我们在每个测试方法中都创建了一个AnonymousSurvey实例，并在每个方法中都创建了答案。
unittest.TestCase类包含方法setUp()，让我们只需创建这些对象一次，并在每个测试方法中使用它们。
如果你在TestCase类中包含了方法setUp()，Python将先运行它，再运行各个以test_打头的方法。
这样，在你编写的每个测试方法中都可使用在方法setUp()中创建的对象了。 

下面使用setUp()来创建一个调查对象和一组答案，供方法test_store_single_response()和test_store_three_responses()使用：
见test_survey.py
"""
