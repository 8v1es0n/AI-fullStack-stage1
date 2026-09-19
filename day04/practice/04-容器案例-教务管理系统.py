"""
    案例:
    开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
        1. 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
        2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
        3. 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
        4. 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
           为空则列出所有学生：遍历所有学生信息并输出。
        5. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
        6. 退出系统。
"""

menu = """
# # # # # # # # # # # # # # # # # # # # # # # # # # 【菜单】 # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  1. 添加学生信息   2. 修改学生信息   3. 删除学生信息   4. 查询学生信息(" "查询所有学生)   5. 统计班级成绩   6. 退出系统  
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
print("欢迎使用教务管理系统 ~")

# 定义一个字典
student_scores = {}

while True:
    print(menu)
    choice = input("请选择要执行的操作(1-6): ")

    # 根据输入的序号,进入不同分支
    match choice:
        # 1. 添加学生信息：根据提示录入学生姓名、
        # 语文、数学、英语成绩，录入完成保存到系统中。
        case "1":
            while True:
                student_name = input("请输入要添加的学生姓名: ")
                if student_name in student_scores.keys():
                    print(f"{student_name} 的信息已存在于系统中, 请重新输入 . . .")
                    continue
                else:
                    break
            chinese_score = float(input("请输入语文成绩: "))
            math_score = float(input("请输入数学成绩: "))
            english_score = float(input("请输入英语成绩: "))
            student_scores[student_name] = {"chinese_score": chinese_score, "math_score": math_score,
                                            "english_score": english_score}
            print(f"{student_name} 的学生信息已添加成功")

        # 2. 修改学生信息：要求输入要修改的学生姓名，
        # 然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
        case "2":
            while True:
                student_name = input("请输入要修改的学生姓名: ")
                if student_name not in student_scores.keys():
                    print(f"{student_name} 的信息不存在, 请重新输入 . . .")
                    continue
                else:
                    break
            chinese_score = float(input("请输入语文成绩: "))
            math_score = float(input("请输入数学成绩: "))
            english_score = float(input("请输入英语成绩: "))
            student_scores[student_name] = {"chinese_score": chinese_score, "math_score": math_score,
                                            "english_score": english_score}
            print(f"{student_name} 的学生信息已修改成功")

        # 3. 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
        case "3":
            while True:
                student_name = input("请输入要删除的学生姓名: ")
                if student_name not in student_scores.keys():
                    print(f"{student_name} 的信息不存在, 请重新输入 . . .")
                    continue
                else:
                    break
            student_scores.pop(student_name)
            print(f"{student_name} 的学生信息已删除成功")


        # 4. 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
        #    为空则列出所有学生：遍历所有学生信息并输出。
        case "4":
            while True:
                student_name = input("请输入要查询的学生姓名: ")
                if student_name == " ":
                    for stu_name, stu_scores in student_scores.items():
                        print(f"学生: {student_name} 的 语文成绩为: {stu_scores["chinese_score"]} "
                              f"数学成绩为: {stu_scores["math_score"]} 英语成绩为: {stu_scores["english_score"]}")
                    break

                elif student_name not in student_scores.keys():
                    print(f"{student_name} 的信息不存在, 请重新输入 . . .")
                    continue
                else:
                    # 单独查询一位同学
                    for stu_name, stu_scores in student_scores.items():
                        if stu_name == student_name:
                            print(f"学生: {student_name} 的 语文成绩为: {stu_scores["chinese_score"]} "
                                  f"数学成绩为: {stu_scores["math_score"]} 英语成绩为: {stu_scores["english_score"]}")
                            print(f"{student_name} 的学生信息已查询成功")
                    break

        case "5":
            # 5. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，
            chinese_list = [chinese for chinese, math, english in student_scores.values()]
            math_list = [math for chinese, math, english in student_scores.values()]
            english_list = [english for chinese, math, english in student_scores.values()]

            max_chinese = max(chinese_list)
            min_chinese = max(chinese_list)
            sum_chinese = sum(chinese_list)
            print(f"语文成绩中, 最高分为: {max_chinese}")
            print(f"语文成绩中, 最低分为: {min_chinese}")
            print(f"语文成绩中, 平均分为: {(sum_chinese /len(chinese_list)):.2f}")

            max_math = max(math_list)
            min_math = max(math_list)
            sum_math = sum(math_list)
            print(f"数学成绩中, 最高分为: {max_math}")
            print(f"数学成绩中, 最低分为: {min_math}")
            print(f"数学成绩中, 平均分为: {(sum_math /len(math_list)):.2f}")

            max_english = max(english_list)
            min_english = max(english_list)
            sum_english = sum(english_list)
            print(f"英语成绩中, 最高分为: {max_english}")
            print(f"英语成绩中, 最低分为: {min_english}")
            print(f"英语成绩中, 平均分为: {(sum_english /len(english_list)):.2f}")

            # 以及语文、数学、英语最高分和最低分的学员姓名。
            chinese_max_name = [name for name, scores in student_scores.items() if scores["chinese_score"] == max_chinese]
            math_max_name = [name for name, scores in student_scores.items() if scores["math_score"] == max_math]
            english_max_name = [name for name, scores in student_scores.items() if scores["english_score"] == max_english]
            print(f"获得语文最高分的是: {chinese_max_name} 最高分为: {max_chinese}")
            print(f"获得数学最高分的是: {math_max_name} 最高分为: {max_math}")
            print(f"获得英语最高分的是: {english_max_name} 最高分为: {max_english}")

            chinese_min_name = [name for name, scores in student_scores.items() if scores["chinese_score"] == min_chinese]
            math_min_name = [name for name, scores in student_scores.items() if scores["math_score"] == min_math]
            english_min_name = [name for name, scores in student_scores.items() if scores["english_score"] == min_english]
            print(f"获得语文最低分的是: {chinese_min_name} 最高分为: {min_chinese}")
            print(f"获得数学最低分的是: {math_min_name} 最高分为: {min_math}")
            print(f"获得英语最低分的是: {english_min_name} 最高分为: {min_english}")

        # 6. 退出系统。
        case "6" | "ESC" | "Esc" | "esc":
            print("感谢您的使用, 希望与你下再次相遇!")
            break
        case _:
            print("输入错误")