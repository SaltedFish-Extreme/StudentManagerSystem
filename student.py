# 定义一个Student类
class Student():
    # 定义魔术方法，初始化学生信息
    def __init__(self, name, age, mobile):
        self.name = name
        self.age = age
        self.mobile = mobile

    # 定义一个打印学生信息的方法
    def __str__(self):
        return f'学生姓名：{self.name},年龄：{self.age},电话：{self.mobile}'

