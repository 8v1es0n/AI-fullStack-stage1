# ----------------------------------------------------------
# 需求1：定义一个函数 is_leap_year，接收一个年份 year（整数），
#       判断该年份是否为闰年，返回 True 或 False。
#
#       闰年规则：
#         - 能被 400 整除的是闰年
#         - 能被 4 整除但不能被 100 整除的也是闰年
#         - 其余不是闰年
#
#       调用该函数，分别判断 2000年、2024年、1900年、2025年 是否为闰年。
# ----------------------------------------------------------

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False

print(is_leap_year(2020))
print(is_leap_year(2020))
print(is_leap_year(1900))
print(is_leap_year(2025))
print("-" * 16)


# ----------------------------------------------------------
# 需求2：定义一个函数 find_best_student，接收一个字典参数，
#       字典格式为 {"学生姓名": 分数, ...}，遍历字典找出分数最高的学生，
#       返回该学生的姓名和分数。
#       
#       调用该函数，传入以下字典并打印结果：
#       {"小明": 88, "小红": 95, "小刚": 72, "小丽": 91, "小军": 84}
# ----------------------------------------------------------

def find_best_student(student_dict):
    for k, v in student_dict.items():
        if v == max(student_dict.values()):
            return k, v
    return None

scores = {"小明": 88, "小红": 95, "小刚": 72, "小丽": 92, "小军": 84}
print(find_best_student(scores))
print("-" * 16)


# ----------------------------------------------------------
# 需求3：定义一个函数 count_case，接收一个字符串参数，
#       统计其中大写字母和小写字母的个数，返回两个结果。
#       （提示：可用字符串的 .isupper() 和 .islower() 方法判断）
#
#       调用该函数，传入字符串 "Hello World! Python3 编程"，
#       用解包方式接收并打印大写字母个数和小写字母个数。
# ----------------------------------------------------------

def count_case(text):
    upper = 0
    lower = 0
    for ch in text:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
    return upper, lower


text1 = "Hello World! Python3 编程"
upper_count, lower_count = count_case(text1)
print(f"字符串：{text1}")
print(f"大写字母个数：{upper_count}")
print(f"小写字母个数：{lower_count}")