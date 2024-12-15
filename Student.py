# 学生类
class Student:
    # 初始化方法
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    # 打印信息方法
    def __str__(self):
        return f"学生姓名：{self.name}，年龄：{self.age}，电话：{self.phone}"
