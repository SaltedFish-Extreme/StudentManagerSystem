from Student import Student


# 学生管理类
class StudentManager:
    def __init__(self):
        # 定义一个学生列表，用来管理保存学生信息
        self.student_list = []

    # 静态方法，输出系统目录
    @staticmethod
    def show_help():
        print('-' * 40)
        print('欢迎您使用学生信息管理系统')
        print('V1.0')
        print('1.添加学生信息')
        print('2.删除学生信息')
        print('3.修改学生信息')
        print('4.查询学生信息')
        print('5.查询所有学生信息')
        print('6.保存学生信息')
        print('7.退出系统')
        print('-' * 40)

    # 加载学生信息方法
    def load_student(self):
        # 打开文件：尝试r打开，如果有异常w
        try:
            f = open('student.data', 'r', encoding='UTF-8')
        except:
            f = open('student.data', 'w', encoding='UTF-8')
        else:
            # 读取数据：文件读取出的数据是字符串还原列表类型；[{}] 转换 [学生对象]
            data = f.read()  # 字符串
            if data == "":
                self.student_list = []
            else:
                new_list = eval(data)
                self.student_list = [Student(i['name'], i['age'], i['phone']) for i in new_list]
        finally:
            f.close()

    # 添加学生信息方法
    def add_student(self):
        # 提示用户输入学生信息
        name = input("请输入学生姓名：")
        age = input("请输入学生年龄：")
        phone = input("请输入学生电话：")
        # 实例化对象，并且追加到学生列表中
        self.student_list.append(Student(name, age, phone))
        print('学生信息添加成功')

    # 删除学生信息方法
    def del_student(self):
        name = input("请输入需要删除的学生姓名：")
        # 遍历学生列表
        for i in self.student_list:
            # 删除学生信息
            if i.name == name:
                self.student_list.remove(i)
                print(f'学生({name})信息删除成功')
                break
        else:
            print("学生姓名不存在")

    # 修改学生信息方法
    def mod_student(self):
        name = input("请输入需要修改的学生姓名：")
        # 遍历学生列表
        for i in self.student_list:
            # 修改学生信息
            if i.name == name:
                i.name = input("请输入修改后的学生姓名：")
                i.age = input("请输入修改后的学生年龄：")
                i.phone = input("请输入修改后的学生电话：")
                print(f'学生信息修改成功，修改后的信息如下：')
                print(i)
                break
        else:
            print("学生姓名不存在")

    # 查询学生信息方法
    def find_student(self):
        name = input("请输入要查询的学生姓名：")
        for i in self.student_list:
            if i.name == name:
                print(i)
                break
        else:
            print("学生姓名不存在")

    # 查询所有学生信息方法
    def findall_students(self):
        if len(self.student_list) == 0:
            print("暂时没有学生信息，请添加后再查询")
        else:
            for i in self.student_list:
                print(i)

    # 保存学生信息方法
    def save_student(self):
        # 把self.student_list转换为字符串保存到student_data文件中
        with open('student.data', 'w', encoding='UTF-8') as f:
            new_list = [i.__dict__ for i in self.student_list]
            f.write(str(new_list))
            print("学生信息保存成功")

    # 定义一个run方法：专门用于实现对管理系统各个功能的调用
    def run(self):
        # 加载文件中保存的学生信息，读取到学生列表中
        self.load_student()
        while True:
            # 显示帮助信息
            self.show_help()
            # 提示用户输入要操作的功能编号
            try:
                num = int(input("请输入要使用的功能序号："))
                if num == 1:
                    self.add_student()
                elif num == 2:
                    self.del_student()
                elif num == 3:
                    self.mod_student()
                elif num == 4:
                    self.find_student()
                elif num == 5:
                    self.findall_students()
                elif num == 6:
                    self.save_student()
                elif num == 7:
                    print("感谢您使用本系统，期待您的下次使用")
                    break
                else:
                    print("您输入的序号有误，请重新输入")
            except Exception:
                print("输入错误，请重新输入")
