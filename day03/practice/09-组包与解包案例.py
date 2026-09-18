"""
    根据如下提供的学生成绩单，完成如下需求：
        1. 计算每个学生的总分、各科平均分，然后一并输出出来。
        2. 统计各科成绩的最低分、最高分、平均分，并输出。
        3. 查找成绩优秀（平均分大于90）的学生，并输出。
"""


students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72)
)

# 1. 计算每个学生的总分、各科平均分，然后一并输出出来。
# 3. 查找成绩优秀（平均分大于90）的学生，并输出。
for stu_id, name, chinese_score, math_score, english_score in students:
    sum_score = chinese_score + math_score + english_score
    avg_score = sum_score / 3
    print(f"姓名为: {name} 的学生, 总分为: {sum_score}, 平均分为: {avg_score:.2f}")
    if avg_score > 90:
        print(f"{name} 同学真优秀!")
print("---------------------------------------------------------------")


# 2. 统计各科成绩的最低分、最高分、平均分，并输出。
# 语文
chinese_list = [student[2] for student in students]
chinese_max = max(chinese_list)
chinese_min = min(chinese_list)
chinese_sum = sum(chinese_list)
print(f"语文的最高分为: {chinese_max}, 最低分为: {chinese_min}, 平均分为: {(chinese_sum / len(students)):.2f}")
# 数学
math_list = [student[3] for student in students]
math_max = max(math_list)
math_min = min(math_list)
math_sum = sum(math_list)
print(f"数学的最高分为: {math_max}, 最低分为: {math_min}, 平均分为: {(math_sum / len(students)):.2f}")
# 英语
english_list = [student[4] for student in students]
math_max = max(math_list)
math_min = min(math_list)
math_sum = sum(math_list)
print(f"英语的最高分为: {math_max}, 最低分为: {math_min}, 平均分为: {(math_sum / len(students)):.2f}")