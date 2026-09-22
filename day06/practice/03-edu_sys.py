# 1. 定义学生类
class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __repr__(self):
        return f"学生: {self.name} 语文成绩: {self.chinese} 数学成绩: {self.math} 英语成绩: {self.english}"



# 2. 定义教务管理系统类
class EduSys:
    def __init__(self):
        self.student_dict = {}

    # 添加学生
    def add_student(self):
        name = input("请输入要添加的学生姓名: ")
        if name in self.student_dict.keys():
            print("学生信息已存在")
            return

        chinese_score = float(input("请输入学生的语文成绩: "))
        math_score = float(input("请输入学生的数学成绩: "))
        english_score = float(input("请输入学生的英语成绩: "))

        if 0 <= chinese_score <= 100 and 0 <= math_score <= 100 and 0 <= english_score <= 100:
            self.student_dict[name] = Student(name, chinese_score, math_score, english_score)
            print("学生信息添加成功")
        else:
            print("输入的成绩有误!")

    # 删除学生
    def del_student(self):
        name = input("请输入要删除的学生姓名: ")
        if name not in self.student_dict.keys():
            print("学生信息不存在")
            return

        self.student_dict.pop(name)
        print("学生信息删除成功")

    # 修改学生
    def update_student(self):
        name = input("请输入要修改的学生姓名: ")
        if name not in self.student_dict.keys():
            print("学生信息不存在")
            return

        # 根据键找到对应的值 , 值的类型属于学生对象
        student = self.student_dict[name]
        print(f"学生数据修改之前信息为{student}")

        chinese_score = float(input("请输入学生新的语文成绩: "))
        math_score = float(input("请输入学生新的数学成绩: "))
        english_score = float(input("请输入学生新的英语成绩: "))

        if 0 <= chinese_score <= 100 and 0 <= math_score <= 100 and 0 <= english_score <= 100:
            self.student_dict[name] = Student(name, chinese_score, math_score, english_score)

            student = self.student_dict[name]
            print(f"学生数据修改后的信息为{student}")
        else:
            print("输入的成绩有误!")

    # 根据名字查询学生
    def get_name_student(self):
        name = input("请输入要查询的学生姓名: ")
        if name not in self.student_dict.keys():
            print("学生信息不存在")
            return

        student = self.student_dict[name]
        print(f"学生当前的信息为{student}")


    # 查询所有学生
    def get_all_student(self):
        values = self.student_dict.values()
        for stu in values:
            print(stu)
        print("查询成功")


    # 运行系统  , 实例方法
    def run(self):
        print("######## 欢迎您访问教务管理系统 ########")
        while True:
            print()
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print("# 1.添加学生   2.修改学生   3.删除学生   4.查询指定学生   5.查询所有学生   6.退出系统   #")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print()

            choice = input("请选择要执行的操作, 输入1-6: ")
            match choice:
                case "1":  # 添加学生
                    self.add_student()
                case "2":  # 修改学生
                    self.update_student()
                case "3":  # 删除学生
                    self.del_student()
                case "4":  # 查询指定学生
                    self.get_name_student()
                case "5":  # 查询所有学生
                    self.get_all_student()
                case "6":  # 退出系统
                    print("Bye ~")
                    break
                case _:  # 其他情况
                    print("输入错误, 请选择1-6之间的菜单功能!")


if __name__ == '__main__':
    management = EduSys()
    management.run()