#   邮箱格式验证
my_email = input("请输入您的邮箱: ")
if my_email.count("@") == 1 and "." in my_email:
    print("符合要求")
else:
    print("格式不合法")