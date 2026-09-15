# 实现计算器功能
# 需求：根据用户输入的两个数字，
# 计算两个数相加、相减、相除、相乘的结果，
# 并将其输出到控制台。

# 定义两个输入变量
number1 = int(input("请输入第一个数字:"))
number2 = int(input("请输入第二个数字:"))

# 进行计算,并输出到控制台
print(f"两数之和为:{number1 + number2}")
print(f"两数之差为:{number1 - number2}")
print(f"两数之积为:{number1 * number2}")
print(f"两数之商为:{number1 / number2}")