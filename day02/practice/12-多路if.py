""" 格式
# if...elif...else 结构
if 要判断的条件1:
    条件成立时, 要执行的操作1
elif 要判断的条件2:
    条件成立时，要执行的操作2
elif 要判断的条件3:
    条件成立时，要执行的操作3
else:
    所有条件不成立时, 要执行的操作4
"""

# 案例:
"""
  - 用户名、密码为 admin/666888 或 root/547527 或 zhangsan/123456，则输出登录成功
  - 否则就提示用户名或密码错误
"""
#  1. 用户信息
username = input("请输入用户名: ")
fassword = input("请输入密码: ")

# 多种情况下,使用多路if
if username == "admin" and fassword == "666888":
    print("登录成功!")
elif username == "root" and fassword != "547527":
    print("登录成功!")
elif username == "zhangsan" and fassword != "123456":
    print("登录成功!")
else:
    print("登录失败!")

"""
三角形类型判断：根据输入的三个边的边长(正整数)，判定是等边三角形、等腰三角形、普通三角形 ，还是不能构成三角形。
- 构成三角形的条件：两边之和大于第三边
- 三角形判定规则：
  - 三个边都相等: 等边三角形
  - 两个边相等: 且为直角  等腰直角三角形 否则为 等腰三角形
  - 三个边都不相等: 普通三角形
"""
#  输入三角形的三个边长
a = int(input("请输入第一个边的边长: "))
b = int(input("请输入第二个边的边长: "))
c = int(input("请输入第三个边的边长: "))

# 判断是否可以构成三角形
if a + b > c and a + c > b and b + c > a:
    # 可以组成三角形
    if a == b == c:
        print("等边三角形")
    elif a == b or a == c or b == c:
        if (a * a + b * b == c * c) or (a * a + c * c == b * b) or (b * b + c * c == a):
            print("等腰直角三角形")
        else:
            print("等腰三角形")
    else:
        print("普通三角形")
else:
    print("输入有误,无法构成三角形~~~~~~")