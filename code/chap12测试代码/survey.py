# 当前版本 ： python3.8.2
# 开发时间 ： 2021/8/27 9:33
class AnonymousSurvey:
    """手机匿名调查问卷的答案"""
    def __init__(self, question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示问卷调查"""
        print(self.question)

    def store_responses(self, new_response):
        """存储单份调查问卷"""
        self.responses.append(new_response)

    def show_results(self):
        """显示收到的所有答卷"""
        print("Survey results: ")
        for response in self.responses:
            print('-' + response)
