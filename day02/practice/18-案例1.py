"""
    - 需求：根据输入的用户名密码执行登录操作
    - 细节：
      1. 正确的用户名和密码为admin/666888 、zhangsan/123456、taoge/888666
      2. 输入用户名和密码进行登录，直到登录成功，程序结束运行; 如果登录失败，则继续输入用户名和密码进行登录
      3. 输入的用户名和密码不能为空！
      4. 登录成功：输出 "登录成功，进入B站首页~"
      5. 登录失败：输出 "用户名或密码错误, 请重新输入!"
"""

while True:
    # 01-录入信息
    username = input("请输入用户名: ")
    password = input("请输入密码: ")

    if username == "" or password == "":
        print("用户名或密码不能为空")
        continue

    # 多种情况下,使用多路if
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
