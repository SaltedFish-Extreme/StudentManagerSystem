# 定义StudentManagerSystem类 具体的操作
from student import Student


class StudentManagerSystem(object):
    # 定义构造方法
    def __init__(self):
        # 定义一个列表，用于保存学生的信息
        self.student_list = []

    # 定义load_student加载学员信息方法
    # 2.8 加载学员信息
    def load_student(self):
        # 1. 打开文件：尝试r打开，如果有异常w
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            # 2. 读取数据：文件读取出的数据是字符串还原列表类型；[{}] 转换 [学员对象]
            data = f.read()  # 字符串
            new_list = eval(data)
            self.student_list = [Student(i['name'], i['age'], i['mobile']) for i in new_list]
        finally:
            # 3. 关闭文件
            f.close()

    # 定义静态方法：输出系统的目录
    @staticmethod
    def show_help():
        print('-' * 40)
        print('V1.0')
        print('1.添加学员信息')
        print('2.删除学员信息')
        print('3.修改学员信息')
        print('4.查询学员信息')
        print('5.遍历所有学员信息')
        print('6.保存学员信息')
        print('7.退出系统')
        print('-' * 40)

    # 添加学员信息的方法
    def add_student(self):
        # 提示用户输入学员信息
        name = input('请输入学员的姓名：')
        age = input('请输入学员的年龄：')
        mobile = input('请输入学员的电话：')
        # 使用Student类实例化对象
        student = Student(name, age, mobile)
        # 调用student_list属性，追加student对象信息
        self.student_list.append(student)
        print('学员信息添加成功')

    # 删除学员信息的方法
    def del_student(self):
        # 提示用户输入要删除的学员姓名
        name = input('请输入要删除的学员信息：')
        # 对student_list属性进行遍历
        for i in self.student_list:
            if i.name == name:
                # 找到要删除的学员，删除
                self.student_list.remove(i)
                print(f'学员{name}信息删除成功')
                break
        else:
            print('你要删除的学员不存在')

    # 修改学员信息的方法
    def mod_student(self):
        # 提示用户输入要修改的学员姓名
        name = input('请输入要修改的学员信息：')
        # 对student_list属性进行遍历，判断要修改的学员姓名是否存在
        for i in self.student_list:
            if i.name == name:
                i.name = input('请输入修改后的学员姓名：')
                i.age = input('请输入修改后的学员年龄：')
                i.mobile = input('请输入修改后的学员电话：')
                print(f'学员信息修改成功，修改后信息如下：学员姓名：{i.name},学员年龄：{i.age}，学员电话:{i.mobile}')
                break
        else:
            print('你要修改的学员信息不存在')

    # 查询学员信息的方法
    def show_student(self):
        # 提示用户输入要查询的学员姓名
        name = input('请输入要查询的学员姓名：')
        # 对student_list属性进行遍历
        for i in self.student_list:
            if i.name == name:
                print(i)
                break
        else:
            print('你要查询的学员信息不存在！')

    # 遍历所有学员信息的方法
    def show_all(self):
        # 直接对列表进行遍历
        for i in self.student_list:
            print(i)

    # 保存学员信息的方法
    # 把self.student_list转换为字符串保存到student_data文件中
    def save_student(self):
        # 1. 打开文件
        f = open('student.data', 'w')

        # 2. 文件写入数据
        # 2.1 [学员对象] 转换成 [字典]
        new_list = [i.__dict__ for i in self.student_list]

        # 2.2 文件写入 字符串数据
        f.write(str(new_list))

        # 3. 关闭文件
        f.close()

        # 提示用户数据已经保存成功了
        print('学员信息保存成功')

    # 定义一个run方法：专门用于实现对管理系统各个功能的调用
    def run(self):
        # 1.调用一个学员加载方法。用于加载文件中的所有学员的信息，加载失败，把得到的所有学员信息保存在student_list属性中
        self.load_student()
        # 2.显示帮助信息，提示用户输入要实现的功能编号
        while True:
            # 显示帮助信息
            self.show_help()
            # 提示用户输入要操作的功能编号
            user_num = int(input('请输入要操作的功能编号：'))
            if user_num == 1:
                self.add_student()
            elif user_num == 2:
                self.del_student()
            elif user_num == 3:
                self.mod_student()
            elif user_num == 4:
                self.show_student()
            elif user_num == 5:
                self.show_all()
            elif user_num == 6:
                self.save_student()
            elif user_num == 7:
                print('感谢你使用通讯录管理系统V1.0，欢迎下次使用！')
                break
            else:
                print('信息输入错误，请重新输入...')
