"""
3. 题目3：集合推导式 + 多集合操作
"""

# 已知四个课外活动小组的成员名单：
calligraphy_set = {"王林", "曾牛", "天运子", "韩立", "厉飞雨", "紫灵", "徐立国"}
painting_set    = {"张铁", "王林", "曾牛", "王蝉", "韩立", "厉飞雨", "云露", "李化元"}
music_set       = {"许木", "红蝶", "韩立", "天运子", "厉飞雨", "曾牛", "虎咆"}
sports_set      = {"遁天", "天运子", "韩立", "姜老道", "紫灵", "云露", "虎咆"}

# 找出同时参加了所有四个小组的学生（四重交集)
result1 = calligraphy_set & painting_set & music_set & sports_set

# 2. 找出参加了书法组，但既没有参加绘画组也没有参加音乐组的学生
result2 = calligraphy_set - music_set - sports_set

# 3. 使用集合推导式找出参加了书法组，但没有参加体育组的学生
result3 = {cs for cs in calligraphy_set if cs not in sports_set}

# 4. 求出所有参赛学生名单（四组并集），并统计总人数
result4 = calligraphy_set | painting_set | music_set | sports_set
print(f"4. 所有参赛学生名单: {result4}")
print(f"   总人数: {len(result4)}")

# 5. 统计每位学生在四个小组中总共出现的次数, 并输出(形式为: xxx 参加了 xxx 个小组)
students = [*calligraphy_set, *painting_set, *music_set, *sports_set]
for stu in students:
    count = students.count(stu)
    print(f"   {stu} 参加了 {count} 个小组")