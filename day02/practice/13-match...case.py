""" 格式
match 数据值:
    case 值1:
        操作1
    case 值2:
        操作2
    case 值3:
        操作3
    case 值4:
        操作4
    ...
    case _:
        操作n
"""

# 需求：实现一个计算器，可以实现+ - * / 运算，用户输入需要运算的两个数以及运算符之后，就可以进行计算。
#  1. 键盘录入
num1 = float(input("请输入数据1: "))
operator = input("请输入运算符: ")
num2 = float(input("请输入数据2: "))

#  match...case模式匹配
match operator:
    case "+":
        print(f"{num1} {operator} {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} {operator} {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} {operator} {num2} = {num1 * num2}")
    case "/" if num2 != 0:
        print(f"{num1} {operator} {num2} = {num1 / num2}")
    case _:
        print("输入有误~~~~~~")