# 定义个人信息变量
name = "刘燕"
age = 19
pro = "软件工程"
hobby = "python"

# 字符串拼接方式1: + 符号
# str(数据): 把数据转换成str类型
message1 = "大家好阿，我是" + name + "，今年" + str(age) + "岁，学习的专业是" + pro + "，爱好" + hobby
print(message1)

# 字符串拼接方式2: %s 占位, 然后再赋值
message2 = "大家好阿，我是%s，今年%s岁，学习的专业是%s，爱好%s" % (name, age, pro, hobby)
print(message2)

# 字符串拼接方式3(推荐使用): f-string
message3 = f"大家好阿，我是{name}，今年{age + 10}岁，学习的专业是{pro}，爱好{hobby}"
print(message3)