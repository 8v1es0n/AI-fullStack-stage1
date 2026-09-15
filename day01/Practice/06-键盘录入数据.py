# input函数 , 录入的数据属于字符串类型
# 把数据转成字符串   str(数据)
# 把数据转成整数    int(数据)
# 把数据转成小数    float(数据)

"""
- 需求：
小智的银行卡中有10000元，现在到ATM进行取钱操作，
请根据输入的金额执行取钱操作，取钱完毕后，展示其银行卡余额。
"""

account = 10000
username = input("请输入账号:")
fwd = input("请输入密码:")
print("操作成功!")
print(f"账户余额为:{account}")

money = input("请输入取款金额:")
print(f"您已成功取出{money},账户余额为:{account - float(money)}")