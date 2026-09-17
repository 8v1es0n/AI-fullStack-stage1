"""
    8. 基于循环语句完成如下需求
"""

# - 需求1：根据输入的直角边的边长，打印等腰直角三角形
for i in range(1, 6):
    for j in range(1, i + 1):
        print("•", end="\t")
    print()

# - 需求2：根据输入的数字，打印对应的数字金字塔
layer_number = int(input("请输入金字塔层数： "))
#  数字金字塔
for num_x in range(1, layer_number + 1):
    for num_y in range(1, num_x + 1):
        print(f"{num_x * num_y}", end="\t")
        if num_x == num_y:
            print()

# - 需求3：打印国际象棋棋盘    ◼◻
for coordinates_x in range(8):
        for coordinates_y in range(8):
            if coordinates_x % 2 != 0 and coordinates_y % 2 != 0:
                print("◼", end="\t")
            elif coordinates_x % 2 != 0 and coordinates_y % 2 == 0 :
                print("◻", end="\t")
            elif coordinates_x % 2 == 0 and coordinates_y % 2 != 0 :
                print("◻", end="\t")
            else:
                print("◼", end="\t")
        print()


"""
9. 根据用户名密码登录
需求：用户名密码登录，正确的用户名和密码为admin/666888 、
zhangsan/123456、taoge/888666, 5次登录机会，输入错误五次，不允许再操作了。
"""
# 方式一: while
count = 5
while count > 0:
    # 用户输入
    username = input("请输入用户名: ")
    password = input("请输入密码: ")
    # 非空判断
    if username == "" or password == "":
        print("输入有误,请重新输入")
        continue  # 跳出本次循环
    # 用户信息判断
    if username == "admin" and password == "666888":
        print("登录成功!")
        break
    elif username == "root" and password != "547527":
        print("登录成功!")
        break
    elif username == "zhangsan" and password != "123456":
        print("登录成功!")
        break
    else:
        print("登录失败,请重新输入!")
        count -= 1
        print(f"剩余重试次数: {count}")

# 方式二: for循环
for c in range(5):
    # 用户输入
    username = input("请输入用户名: ")
    password = input("请输入密码: ")
    # 非空判断
    if username == "" or password == "":
        print("输入有误,请重新输入")
        continue  # 跳出本次循环
    # 用户信息判断
    if username == "admin" and password == "666888":
        print("登录成功!")
        break
    elif username == "root" and password != "547527":
        print("登录成功!")
        break
    elif username == "zhangsan" and password != "123456":
        print("登录成功!")
        break
    else:
        print("登录失败,请重新输入!")
        print(f"剩余重试次数: {4 - c}")


"""
10. 将1-1000之间（含1000）所有的5的倍数的数字累加起来。
"""
sum = 0
for num in range(1,1001):
    if num % 5 == 0:
        sum += num
print(sum)

print()
print("------------------------------------------选做----------------------------------------------------------")

# 统计字符串 "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd" 字符串中有多少个a和k。
str_a = 0
str_k = 0
for str in "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd":
    if str == "a":
        str_a += 1
        continue
    if str == "k":
        str_k += 1
        continue
print(f"str_a 的数量为：{str_a}   str_k 的数量为： {str_k}")


"""
    12. 编写程序，接收用户输入一个整数，判断：
      - 如果是正数且偶数，输出“正偶数”
      - 如果是正数且奇数，输出“正奇数”
      - 如果是负数且偶数，输出“负偶数”
      - 如果是负数且奇数，输出“负奇数”
      - 如果是0，输出“零”
    要求：分别用 if-elif-else 和 match-case 各写一版
"""
# if-elif-else版
int_num = int(input("请输入一个整数："))
if int_num > 0 and int_num % 2 == 0:
    print(f"{int_num} 这个数为： 正偶数")
elif int_num > 0 and int_num % 2 == 1:
    print(f"{int_num} 这个数为： 正奇数")
elif int_num < 0 and int_num % 2 == 0:
    print(f"{int_num} 这个数为： 负偶数")
elif int_num < 0 and int_num % 2 == 1:
    print(f"{int_num} 这个数为： 负奇数")
elif int_num == 0:
    print("零")
else:
    print("输入有误")

# match-case版
match int_num:
    case 0:
        print("零")
    case num if num > 0 and num % 2 == 0:
        print("正偶数")
    case num if num > 0 and num % 2 != 0:
        print("正奇数")
    case num if num < 0 and num % 2 == 0:
        print("负偶数")
    case num if num < 0 and num % 2 != 0:
        print("负奇数")


"""
    13. 接收用户输入的身高（米）和体重（公斤），计算 BMI = 体重 / 身高²，并输出健康建议： 【选做】
      - BMI < 18.5：偏瘦
      - 18.5 ≤ BMI < 24：正常
      - 24 ≤ BMI < 28：偏胖
      - BMI ≥ 28：肥胖
    使用 if-elif-else 实现，并对输入异常（如身高为0或负数）做提示。
"""
# 用户输入基本信息：
height = float(input("请输入身高（米）: "))
weight = float(input("请输入体重（公斤）: "))

# 输入异常检查
if height <= 0:
    print("错误：身高必须为正数！")
elif weight < 0:
    print("错误：体重不能为负数！")
# 输入合法
else:
    bmi = weight / (height ** 2)
    print(f"BMI = {bmi}")
    # BMI判定
    if bmi < 18.5:
        print("健康建议：偏瘦")
    elif bmi < 24:
        print("健康建议：正常")
    elif bmi < 28:
        print("健康建议：偏胖")
    else:
        print("健康建议：肥胖")


"""
    14. 模拟银行取款机  
    初始余额为 10000 元，循环显示菜单：
    1. 查询余额
    2. 存款
    3. 取款
    4. 退出
"""
print("欢迎您使用本银行业务系统")
sys_money = 10000.0

while True:
    print("""\t1. 查询余额\n\t2. 存款\n\t3. 取款\n\t4. 退出""")
    sys_num = int(input("请输入对应业务数字，以继续: "))
    if sys_num == 1:
        print(f"您的账户余额为： {sys_money} 元")
        print("---------------------------------------------------------")
        continue
    if sys_num == 2:
        deposit_money = float(input("请输入您要存入的金额："))
        sys_money += deposit_money
        print(f"您已成功存入： {sys_money} 元")
        print("---------------------------------------------------------")
        continue
    elif sys_num == 3:
        takeOut_money = float(input("请输入您要取出的金额："))
        if sys_money < takeOut_money:
            print(f"取出操作无法完成，当前余额为: {sys_money}")
        sys_money -= takeOut_money
        print(f"您已成功取出： {sys_money} 元")
        print("---------------------------------------------------------")
        continue
    else:
        print("您已成功推出")
        break


"""
    15. 简易计算器（支持循环计算，用 match-case）  
    用户输入两个数字和一个运算符（+ - * /），输出计算结果。
    计算完成后询问：“是否继续计算？(Y/N)”，输入 Y 或 y 继续，n 或 N 退出。
    - 要求：
      - 除法时判断除数是否为 0
      - 运算符不匹配时提示“不支持的操作”
"""
# 循环计算
while True:
    # 1。 用户输入
    num1 = float(input("请输入第一个数字： "))
    operator = input("请输入运算符： ")
    num2 = float(input("请输入第一个数字： "))
    # 分支判断
    match operator:
        case  "+" :
            print(f"{num1} {operator} {num2} = {num1 + num2}")
        case  "-" :
            print(f"{num1} {operator} {num2} = {num1 - num2}")
        case  "*" :
            print(f"{num1} {operator} {num2} = {num1 * num2}")
        case  "/" :
            # 除数非零判断
            if num2 != 0:
                print(f"{num1} {operator} {num2} = {num1 / num2}")
            else:
                print("除数不能为 0")
                continue
        case _:
            print("不支持的操作")
    # 分支结束后，提示
    status = input("是否继续计算？(Y/N)")
    match status:
        case "Y" | "y":
            break
        case "N" | "n":
            continue


"""
    16. 猜数字加强版（固定次数 + 提示剩余次数） 
    - 需求：系统随机生成一个1-100之间的整数，用户有5次猜测机会。每次猜测后：
      - 猜中：输出“恭喜！猜中了！”并结束
      - 猜错：提示“猜大了”或“猜小了”，并显示剩余次数
      - 5次都没猜中：输出“游戏失败，正确数字是X”
"""
import random
# 取值范围
start = 1
end = 100
# 随机生成一个1 ~ 100 的数字
lucky_number = random.randint(1, 100)

# 5次尝试机会
for number in range(5):
    test_number = int(input("请输入一个幸运数字： "))
    if start < test_number < lucky_number:
        print(f"{test_number} 小了")
        start = test_number + 1
        print(f"你还有 {4 - number} 次机会")
        print(f"当前范围为： {start} ~ {end}")
        continue
    elif lucky_number < test_number < end:
        print(f"{test_number} 大了")
        end = test_number - 1
        print(f"你还有 {4 - number} 次机会")
        print(f"当前范围为： {start} ~ {end}")
        continue
    elif lucky_number == test_number :
        print("你中奖了！ 你中大奖了！！！")
        break
    else:
        print("输入不合法")
